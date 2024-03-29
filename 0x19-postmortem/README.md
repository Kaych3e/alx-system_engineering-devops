
# Postmortem: Outage Incident Report
> A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

To provide the rest of the companys employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

![1684863953632](https://github.com/Kaych3e/alx-system_engineering-devops/assets/113714466/3fe6d23f-a661-4145-974f-735f73bcd466)


## Table of contents
* [Issue Summary](#Issue Summary)
* [Timeline](#Timeline)
* [Corrective and Preventative Measures](#Corrective and Preventative Measures)
* [Conclusion](#Conclusion)

## Issue Summary
Duration: June 9, 2023, 10:00 AM to June 10, 2023, 2:00 PM (PST)
Impact: The GadgetHub online shopping service experienced an outage, rendering it inaccessible to users. Users attempting to access the service received error messages and were unable to make purchases. The outage affected 100% of the user base, leading to significant revenue loss.
=======

## Timeline
Issue Detected: June 9, 2023, 10:00 AM (PST)
Issue Detection: Monitoring system triggered an alert for the unresponsiveness of the online shopping service.
Actions Taken: The incident response team initiated an investigation, focusing on the backend infrastructure and network connectivity.
Misleading Investigation: Initially, the team suspected a network issue, leading to extensive debugging of network components.
Escalation: The incident was escalated to the infrastructure team for further analysis and resolution.
Incident Resolution: The root cause was identified, and corrective measures were implemented to restore the service.
Root Cause and Resolution:
Root Cause: The outage was caused by a database failure. A critical table in the database became corrupted, resulting in an unresponsive state of the entire system.
Resolution: The incident response team restored the service by performing a database rollback to a previous stable state. The corrupted table was repaired, and data integrity checks were implemented to prevent similar incidents in the future.

## Corrective and Preventative Measures
* Improvements:
Implement automated database health checks to proactively identify and address potential issues.
Enhance monitoring capabilities to detect database failures and corruption promptly.
Regularly test and validate database backups to ensure their reliability for quick recovery.

* Tasks to Address the Issue:
Develop and deploy automated database health checks with appropriate alerting mechanisms by July 31, 2023.
Enhance monitoring by implementing real-time checks for database performance and availability by August 15, 2023.
Conduct monthly database backup tests, including validation of data integrity, by July 15, 2023.
Review incident response procedures to streamline the escalation process and improve coordination among teams by July 31, 2023.

## Conclusion
The outage was caused by a database failure, resulting in a complete service outage for the online shopping platform. The incident response team acted promptly to investigate and resolve the issue, restoring the service within the expected timeframe. To prevent similar incidents in the future, proactive measures will be implemented, including automated database health checks, enhanced monitoring capabilities, and regular validation of database backups. By addressing these tasks, we aim to improve the reliability and resilience of our system, ensuring uninterrupted service for our users.
