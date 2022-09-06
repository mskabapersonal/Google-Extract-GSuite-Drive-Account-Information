echo off

set customer_ids=%1


(for %%a in (%customer_ids%) do (
   echo running %%a
   set CUSTOMER_ID=%%a
   gam all users show filelist name filesize > %%a.csv
)) 

