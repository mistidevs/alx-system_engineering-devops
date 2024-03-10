# 5xx Error on Apache WordPress Website (A Postmortem)

## Issue Summary

The issue transpired from 6:30 PM to 10:30 PM EAT on Friday 1st March 2024. This was soon after the developers had pushed a major update that greatly reduced latency for API calls packing an extremely smooth UI/UX experience to go with it. This bug affected 100% of users. Users saw a 5XX error indicating that the web server had some internal resolution issues. The entire website could not be accessed since the issue was because there was a misspelling in the settings.php file for the entire website. Rather than resolving to .php files the misspelling resolved to .phpp files.

## Timeline

**6:30 PM EAT:** The engineers deployed the code to production and were ready to have an amazing weekend.
**7:00 PM EAT:** Users began to question whether their internet was the issue and were restarting their routers and writing emails ranging from concern to frustration to anger.
**7:30 PM EAT:** The weekend for the engineers was interrupted and they connected to the company VPN to attempt to debug the issue.
**8:30 PM EAT:** After an hour one engineer assumed that the issue was that there was no .html file (from the output of strace).
**8:45 PM EAT:** An implementation with a .html file was pushed to production. This solved the 5xx error but the whole website was just one static HTML page.
**10:15 PM EAT:** After 1 and a half hours a junior developer who had been recently promoted from an intern was looking through the files.
**10:18 PM EAT:** He noticed that the settings.php file resolved to .phpp files rather than .php files.
**10:20 PM EAT:** He raised this concern which was confirmed and quickly corrected with the .html file being deleted.
**10:25 PM EAT:** The code was pushed to production.
**10:30 PM EAT:** The problem was fixed and users stopped complaining.

## Root Cause & Resolution

The root cause was that when configuring settings for the WordPress site the developers in charge of the back-end configurations made a spelling error by resolving traffic to .phpp files rather than .php files. For example, one line with an issue was:

`require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );`

Hence, a the solution was entering the file and removing the extra p's present. Otherwise, the following sed command could be used for automation enhancing:

`sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php`

## Corrective and Preventive Measures
To ensure that this error does not happen in the future- or that it will happen with less frequency- the developer team will ensure they are well rested and always proofread each other's work. Moreover, after deploying to production automated tests will be deployed for a period of 15 minutes to ensure the deployment is stable and error free. Nonetheless, to err is human. Notwithstanding, the team will perfect the art of seldom erring.
