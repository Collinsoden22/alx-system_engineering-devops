# ** ISSUE SUMMARY **

On Wednesday, 31st of November, 2022 at about 2:06pm (GMT+1), Mymediconnect experienced an outage in payment which is as a result of something that seems like a bug with the payment system implemented. All payments made by the period within which the incidence occured were not captured, thereby resulting to lost of payment receipts.. The outage started at about 2:06pm (GMT+1) up to 6:00pm (GMT+1).



## Timeline
2:06pm  (GMT+1) - Outage began 
2:26pm (GMT+1) - Staff were notified by a super ticket from one of the customers that made payments.
2:27pm (GMT+1) - 2:30pm (GMT+1): Staff began incestigation/confirmation of reports from customers.
6:00pm (GMT+1) - Outage resolved.


## Root Cause
The payment gateway was not sending webhook to the url it ought to, hence payments were not captured.

When user made payment, the payment goes through but the system did not recieve the payment confirmation from the payment system implemented, hence the system still held that payment was not made by an account even when receipts are issued. When we noticed, we tried verfiying the claims, comparing receipts IDs with that from the support tickets we got, we noticed that it happened for some group of persons. We sent them a mail to confirm if the issue was from them, we then realized that the system was not verifying the transactions as user spent more than the required time on a page when making payments.

# Resolutions
### We were able to resolve the receipts issue my manually updating payment statuses
### We adviced users not to close the payment page immediately after payment
### We also ensured that all payments are verified by using the payment system authorization and verification mechanism
### We also ensured that all APIs are tested properly before pushing to a production environment.
