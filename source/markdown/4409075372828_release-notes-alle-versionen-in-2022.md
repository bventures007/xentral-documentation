> **Tipp**
>
> Für jede XentralRelease gibt es einen eigenenCommunity-Thread. Solltest du beim Update irgendwelche Probleme haben, sieh bitte in der Community nach - dort findest du Informationen und kannst jederzeit deine Probleme melden.

> **Anmerkung**
>
> Updates von einer XentralVersion 21.x oder älter auf die aktuellste XentralVersion können eine längere Zeit in Anspruch nehmen - abhängig von der Menge an Daten in deiner XentralInstanz. Bitte habe etwas Geduld.

> **Wichtig**
>
> Prüfe vor dem Update, ob eswichtige Update Informationgibt, die für dich relevant sind.

Suchst du die[aktuellen Release Notes aus 2023](https://help.xentral.com/hc/de/articles/7280352216860#UUID-f92f41f2-aade-23a8-0517-3485665faace)?

## 22.5 Release and Patch Releases

### Patch Version 22.5.12

*Release date: 4-January-2023 *#### Bug fixes **Shopware 6 (ECOM-1658)** Issues with establishing the connection to Shopware 6 have been fixed. ** Magento 2 (ECOM-1659)** During the automatic order import from Magento the order number was overwritten with the order ID. This has been fixed. ** finAPI (FAC-1659)**

The problem with the login button for renewing the consent has been fixed.

### Patch Version 22.5.11

*Release date: 3-January-2023 *#### Bug fix **Shopify (ECOM-1661)**

The Shopify adapter package was updated to the newest version to support the new Shopify version.

### Patch Version 22.5.10

*Release date: 3-January-2023 *#### Bug fixes **API (PIM-996)** Security fixes for the Standard XML API have been added. ** Hubspot (TAN-2798)**

Contacts without owner ID could not be imported. This has been fixed.

### Patch Version 22.5.9

This patch reverts an unfinished Amazon SP API change.

### Patch Version 22.5.8

*Release date: 21-December-2022*

#### Bug fixes

We have fixed the 500 error during the item scan in dispatch center.

**Shopify (ECOM-1469)** We have removed the deprecated ** value_type** field to prepare for Shopify Online Store 2.0 breaking changes.

### Patch Version 22.5.7

*Release date: 19-December-2022 *#### Bug fix **Shopimporter (ECOM-1496)**

We added a content header to better support the image export to Shopware 6.

### Patch Version 22.5.6

*Release date: 16-December-2022 *#### Bug fix **Shopimporter (AMAZON-1748)**

We have fixed an issue with the Amazon shopimporter where the tax rate was returned as an incorrect numeral value. The order import in Amazon now works as expected.

### Patch Version 22.5.5

*Release date: 14-December-2022 *#### Bug fixes **Employee administration (TAN-2767)** Users can now select the year 2023 when adding vacation days. ** Fullfilment (FHPB-3)** The state and country are now assigned to the contact person that is directly created in the receipt. ** Fulfillment (FFU-1279)** The issue that prevented users from creating shipping labels if discount items were part of the order is now fixed. ** Xentral NextGen (PIM-935)** Fixed the column sorting issue. ** DATEV (FAC-1623)** We have fixed the export issue in the DATEV financial export module. ** Fulfillment (FFU-1104)** We have fixed the link to the Help Center in the return order module. ** Fulfillment (FHPB-16)** Labels for delivery notes now display the correct data. ** Fulfillment (1064)** Fixed the issue with the special fields ** Fulfillment (FFU-977)** When relocating items with serial numbers, the storage of the serial numbers now updates properly. ** Fulfillment (FHPB-4)** The date in the ** Delivery date **column can now be saved. ** Fulfillment (FHPB-10)** Fixed the issue where batches were stocked incorrectly after the cancellation of a delivery note. ** Fulfillment (FHPB-38)** We have removed theSerial number assistantbutton. ** Fulfillment (FHPB-5)** Special characters are now displayed on in the own and external task description fields when converted to PDF. ** DATEV (FAC-586)** We have fixed an issue with manually inserting the concatenated account and booking key number in the bank transaction. ** finAPI (FAC-1612)**

If the bank connected to finAPI requires a renewal of credentials, a message will display in the account and on the payment transaction import page.

#### Improvements **API (PIM-840)** Added the ** Create Product **endpoint to the new Xentral API. ** Xentral NextGen (PIM-772)** You can now check your subscription status in the side menu. ** Xentral NextGen (PIM-768)** We have optimized the launchpad feature for mobile users. ** Fulfillment (FHPB-2)** It is now possible to create carrier shipment labels with amounts smaller than 1. ** Fulfillment (FFU-1120)** We have improved loading times when scanning items in the dispatch center. ** Fulfillment (FFU-1273)**

The service order module is now available on new instances.

### Patch Version 22.5.4

*Release date: 09-December-2022 *#### Improvements **API (FAC-1561, FAC-1601)**

We have added a new API endpoint for exporting the credit note list as a CSV file. The new API endpoint also contains tags.

#### Bug fixes **Online shops (ECOM-1630)** We have fixed database connection errors for several online shop interfaces. ** Tax (FAC-1244)** The VAT-ID check in the Address module now works for all EU country codes. ** Invoice (FAC-812)** The debtor number in invoice now saves properly. ** DATEV (FAC-1615)**

We have fixed an issue with double invoice numbers being imported to Xentral.

### Patch Version 22.5.3

*Release date: 08-December-2022 *#### Bug fix **Shopify (ECOM-1627)**

The issue with the 500 error message appearing when importing orders is now fixed.

### Patch Version 22.5.2

*Release date: 08-December-2022*

This patch contains fixes for hiding the license notification and reducing MySQL connections.

### Patch Version 22.5.1

*Release date: 07-December-2022 *#### Improvements **Performance ** We have introduced several significant performance improvements. **API ** We have optimized the performance of the API `v1/belege/auftraege` and `v1/belege/liefernscheine`. **Shopify POS (ECOM-1528)**

When orders with only an email address (no other customer data) are imported from Shopify POS, they are overwritten with the default customer for Shopify POS from the shop importer settings. If no default customer is set, they will be ignored.

### Release Version 22.5.0

*Release date: 06-December-2022 *#### New features **Free trial (PIM-852)**

The free trial instances are now populated with the demo data and a notification at the top of the screen.

#### Improvements **Xentral NextGen (PIM-860)** The business insight widgets are now only visible to the users with admin permissions. ** Translation (FFU-1137)** All elements of the order proposal module are now translated. ** API (FFU-1011)** We have added a new warehouse API endpoint that enables you to retrieve an item from a storage location in any warehouse. ** Purchase order (FFU-706)** The editor field in the purchase order module is now editable. ** Follow-up (FFU-1152)**

We have removed the dashboard tab from the follow-up module.

#### Bug fixes **Xentral NextGen ** Users can now access Basic Settings via SmartSearch. **Shopware (ECOM-1549)** The Shopware stock sync issue is now fixed. ** Shopware (ECOM-1539)** The issue preventing sales orders with the payment status "pending" from being imported to Xentral is now fixed. ** Invoices (FFU-1198)** We have fixed an issue with creating double invoices in the auto-dispatch process. ** Warehouse (FFU-1155)** Returns to supplier stock count issue is now fixed and the stock item number is reduced correctly. ** Dispatch center (TAN-2618)**

Error messages and logouts from dispatch center have been fixed.

## 22.4 Release and Patch Releases

### Patch Version 22.4.26

*Release date 29-November-2022*

This patch contains a fix for the adapter box.

### Patch Version 22.4.25

*Release date 23-November-2022 *#### Bug fix **Security (SRE-978)**

Critical security issue resolved.

### Patch Version 22.4.24

*Release date 22-November-2022 *#### Bug fix **POS (FAC-1592)**

The date error in the monthly report for the POS module combined with fiskaly is now fixed.

### Patch Version 22.4.23

*Release date 17-November-2022 *#### New feature **Free trial (PIM-852)**

The free trial instances are now populated with the demo data and a notification at the top of the screen.

#### Bug fix **Xentral NextGen (PIM-862)**

Users can now access Basic Settings via SmartSearch.

### Patch Version 22.4.22

*Release date 16-November-2022 *#### Improvement **Xentral NextGen (PIM-860)**

The business insight widgets are now only visible to the users with admin permissions.

### Patch Version 22.4.21

*Release date 15-November-2022 *#### Bug fix **FTP Backup (TAN-1620)**

We have improved the stability of the data backup process in the FTP backup module.

### Patch Version 22.4.20

*Release date 14-November-2022 *#### Bug fix **Shopware (ECOM-1549)**

The Shopware stock sync issue is now fixed.

### Patch Version 22.4.19

*Release date 11-November-2022 *#### Bug fix **Shopify (ECOM-1539)**

The issue preventing sales orders with the payment status "pending" from being imported to Xentral is now fixed.

### Patch Version 22.4.18

*Release date 10-November-2022 *#### Improvements **API**

Minor update in the API contract, to ensure consistency in naming.

### Patch Version 22.4.17

*Release date 09-November-2022 *#### Improvements **Apps (PF-874)**

Customers who migrated to the new payment management system can now test apps for 30 days. After the 30-day-trial period the app is automatically converted to a paid subscription and you can manage it the My Licenses page.

#### Bug fixes **Shopify (ECOM-1523)** The order import issue in Shopify POS is now fixed. ** Shopify (ECOM-1529)**

The sales order import issue when the address line 1 on the sales order was empty is now fixed.

### Patch Version 22.4.16

*Release date 03-November-2022 *#### New feature **General (TAN-2405)** Cloud customers can now request a password reset from the login screen. On the login screen, click ** forgot password**, enter your email address and you will receive a password reset link.

#### Improvements **Shopware 6 (ECOM-669)**

We have enabled bulk operations within product sync.

### Patch Version 22.4.15

*Release date 27-October-2022 *#### Bug fixes **Shopify POS (ECOM-1516)** New customers imported through the Shopify POS sales order import with only a name, surname, and email address, could not be created in Xentral. This has now been fixed. ** Amazon (AMAZON-1644)**

Edge case scenarios for Amazon order/tracking status synchronization were fixed.

### Patch Version 22.4.14

*Release date 26-October-2022 *#### Improvements **Shopify POS (ECOM-1490)** Customer matching for customers imported with Shopify POS sales orders has been improved. ** Shopify (ECOM-1453)** By removing the video from the onboarding wizard, the onboarding experience for Shopify Public App users has been improved. ** Shopware 6 (ECOM-669)**

The bulk export of products to Shopware 6 has been improved to increase performance.

#### Bug fixes **Sendcloud/DHL 3.0 (FFU-1002)** You can now correct the recipient address data during label printing, when there is an error in the address data in the delivery note. ** Shopify (ECOM-1498)**

The 500 error when importing sales orders has been fixed.

### Patch Version 22.4.13

*Release date 21-October-22*

With this patch feature flags were adjusted.

### Patch Version 22.4.12

*Release date 19-October-2022 *#### New feature **Shopify (ECOM-1439)** You can now select a standard customer for POS sales orders ("walk-in customer") if a sales order from Shopify POS doesn't contain a customer. This feature will be released with a feature flag. If you want to test it please approach our customer success with your 16-digit license number and ask to add you to the beta testing group. ** Shopify (ECOM-1394)**

This first iteration of our new Shopify POS feature allows you to import sales orders (SO) from Shopify that are created via Shopify POS and are already fulfilled.

Functionality: Import SOs that are already paid, fulfilled and are created via Shopify POS and do not have a customer

Out of scope/ part of later iterations:

- Shopify POS SOs with a customer
- Shopify Onlineshop SOs with fulfilled line items (partially fulfilled SO)
- Shopify Onlineshop SOs that are completely fulfilled and in the past (historical SOs)

This feature will be released with a feature flag. If you want to test it please approach our customer success with your 16-digit license number and ask to add you to the beta testing group.

#### Bug fix **Shopware 6 (ECOM-1483)**

The issue with advanced prices being deleted every time the item is exported to the shop is now fixed.

### Patch Version 22.4.11

*Release date 12-October-2022 *#### New feature **Email accounts (TAN-2457)** You can now add your Microsoft 365 email accounts using OAuth in just a few clicks. You can find more information in our academy and handbook. ** Hubspot (TAN-2458)**

You can now use OAuth for the Hubspot integration.

### Patch Version 22.4.10

*Release date 05-October-2022 *#### New feature **DHL 3.0 (FFU-852)**

You can now print shipping labels for the Warenpost International Premium service.

#### Bug fixes **Shopware6 (ECOM-1298)** The price inheritance from parent product to child product for matrix products has been removed. All options/variants are now transferred to Shopware with their own prices. ** Purchase orders (FFU-668)**

The quick preview for purchase orders in draft mode could not be opened. This has been fixed now.

### Patch Version 22.4.9

*Release date 28-September-2022 *#### Bug fixes **Revert from FFU-1034**

The issue with printer spoolers not running is now fixed.

### Patch Version 22.4.8

*Release date 27-September-2022 *#### New features **Fulfillment (FFU-927)**

You can now define a group of return centers (recipient address of return shipping labels) in the Settings tab of the return order module. You must use the group module for this purpose. This ensures that only addresses defined in this group can be selected as the recipient for a returned order. You can additionally define a default return center which automatically populates the recipient address in a newly created return.

If none is defined, Xentral continues to fall back on the company address in basic settings to populate the recipient of a return shipping label.

**User settings (PF-800)**

You can now enable service accounts that allow our customer support team access to your instance in order to troubleshoot issues and provide faster support

#### Bug fix **DHL 3.0 (FFU-1063)** The issue with missing states in international shipping labels is now fixed. ** Mobile device users (PIM-535)**

The navigating issue when using Xentral on your mobile device is now fixed.

### Patch Version 22.4.7

*Release date 20-September 2022 *#### New features **DHL 3.0 (FFU-900)** The branch rerouting option (Filial-Routing) has been added for DHL 3.0. This option is only available in Germany. ** DHL 3.0 (FFU-809)**

With DHL 3.0 you can now create shipping labels for bulky goods (Sperrgut).

#### Bug fixes **DHL Express (FFU-964)**

Shipping labels could not be printed when the name contained special characters. This has now been fixed.

### Patch Version 22.4.6

*Release date 13-September-2022 *#### Improvements **OAuth (TAN-2381)**

In the OAuth module you can now view authorized accounts and delete tokens. You can create new tokens directly in the individual modules (for example, for the connection to Microsoft 365 email accounts using OAuth). When you authorize the token, it will be automatically created in the background and linked to the email backup account.

### Patch Version 22.4.5

*Release date: 08-September-2022*

This patch includes minor bug fixes.

### Patch Version 22.4.4

*Release date: 02-September-2022 *#### Improvement **Sendcloud (FFU-828)**

When creating a new Sendcloud shipping method, some often used settings are now pre-selected to save time.

#### Bug fixes **Sendcloud (FFU-966)** Issue with the creation of shipping labels has been fixed. ** Sendcloud (FFU-968)**

Issue where the standard weight was not considered has been fixed.

### Patch Version 22.4.3

*Release date: 02-September-2022 *#### Improvements **Online Shops (ECOM-1219)** Starting with this release, every Shop/ Marketplace will be in ** Import-Mode "Demo"** after setup. This way we want to reduce the risk of accidentally syncing data between Xentral and their Shop/ Marketplace.

#### Bug fixes **Shopify (ECOM-1368)**

The issue with customer address being added to the additional shipping address in Xentral when only one address is available in Shopify is now fixed.

### Patch Version 22.4.2

*Release date: 23-August-2022 *#### Improvements **Shopware 6 (ECOM-1324)** The Shopware 6 payload in Smarty was extended. ** Letterhead settings (TAN-1876)**

A preview was added to theLetterheadtab in the basic settings. ClickingSavewill make the changes visible immediately.

#### Bug fixes **Email accounts (TAN-2304)** The functionality to test an email configuration has been fixed. Clicking the buttontest connectionchecks whether the IMAP settings are correctly configured by sending a test mail. ** SuperSearch (TAN-2303)**

The quick overview for addresses, documents, and products in the SuperSearch has been fixed.

### Patch Version 22.4.1

*Release date: 18-August-2022 *#### Bug Fixes **Amazon shopimporter (AMAZON-894)** Amazon orders were not imported. This has been fixed. ** Amazon shopimporter (AMAZON-900)** Provide characterization test for Shopimporter_Amazon::amazonOrderToWaWi ** Amazon sales orders and invoices (FAC-767)**

Amazon sales orders and invoices were created with a wrong VAT tax rate (20.1%). This has been fixed.

#### Known issues

Some translation strings in the English version might be defected in this version. They will be fixed right away with the 22.4.2 version.

### Release Version 22.4.0

*Release date: 04-August-2022 *#### New features **Deletion of tickets (TAN-1901)** You can now delete tickets in the ticket module. This is a hard delete of tickets and it will help you to adhere to GDPR regulations. ** Sendcloud return handling (FFU-243)** Returns can now be handled via Sendcloud: Xentral is now able to create return labels for Sendcloud. ** Shopify sales order comparison (ECOM-685)** You can now compare the number of sales orders in Shopify with the number of sales orders created in Xentral. The Compare sales orders feature compares the sales orders from the last 7 days and reports their number. In addition, if the numbers of sales order in Shopify and Xentral differ, the Shopify sales orders that have not been imported into Xentral will be listed by their Shopify sales order IDs. ** Liability import via transfer module (TAN-687)**

Liabilities can now be imported via the transfer module. To this end, you can now create a new type of transfer account called liabilities. Then you can select liabilities in the Import Documents section and import a corresponding XML file. The imported liabilities will then appear in the liabilities module.

#### Improvements **Maintenance mode (TAN-2011)** We have introduced a so-called maintenance mode that comes into effect during any update. In maintenance mode, users cannot access the Xentral application and interfere with running processes. ** API in maintenance mode (TAN-2116)** When Xentral is in maintenance mode, all API endpoints are disabled. The API endpoints are disabled so that no data can be written into the database during a migration process. ** CSRF (cross-site request forgery) prevention (TAN-1967)** Your session token will become invalid upon your Xentral logout. This reduces the risk of your session token being used by third parties. ** Business letter templates (TAN-1877)** All predefined business letter templates are now available for each new project that you set up in Xentral. ** Kaufland (ECOM-981)** We have added identification to the API call header for Kaufland. ** Countries and states (GTM-233)** The drop-down lists for countries and states have been aligned across the application and in accordance with ISO codes and standards. ** Translations (GTM-248)** The list of product categories is now available in English as well. ** Product tree (TAN-488)**

If an item category contains subcategories and you delete the main category, the application behavior has been improved: You will be prompted that the category you wish to delete contains subcategories and you can confirm or cancel the deletion. If you confirm the deletion, the category and all subcategories will be deleted.

#### Bug fixes **Wiki (TAN-1907)** The content of the wiki was not visualized anymore and pages were created twice. This has been fixed. ** Placeholder translations (GTM-511, GTM 329)** Missing translations in item tree and shipping methods: Some user interface elements such as names of fields did not have English translations and therefore internal names were shown. ** User interface (TAN-1582)** In some cases, the names of check boxes were not displayed at all. ** Welcome page (TAN-1531)** The Edit Favorites button on the Welcome page did not work. ** Shopware 5 (PIM-298)** Export of articles to Shopware 5 failed. This happened only for articles imported via CSV into Xentral. ** Shopware 6 (ECOM-791)** The Suppress product text transmission option did not work. ** Provision (TAN-1634)** In the Provision module page in the app store, the link to the help center was missing. ** Payroll (TAN-1635)** In the Payroll module page in the app store, the link to the help center was missing. ** Shopify (ECOM-435)** In case of variant products that are no matrix products, the export and update of these products to Shopify did not work. ** Shipping rules (FFU-413)**

Due to fields being deleted or cleared after saving, shipping rules could not be created.

#### Removals **API method removals (PIM-446, PIM-445, PIM-420, PIM-390)**

The following ERP API methods have been removed:

- KundeMitUmsatzsteuer
- LagerID
- LagerzahlenCSV
- LieferdatumEinkauf
- LieferscheinCheck
- LoadInventurStandardwerte
- LoadReisekostenStandardwerte
- LogWithTime
- MahnwesenBetrag
- MailSendNoBCC
- ManuelEcho
- NavigationENT
- IsArtikelInZwischenlager
- InventurProtokoll
- html_entity_decode_utf8
- hex_dump
- GetZwischensummenSort
- GetZwischenSummebisSort
- GetWarteschlangeTicketWiedervorlage
- GetWarteschlangeTicketAlle
- getUmlauteArray
- GetNavigationSelect
- GetPhoneLink
- GetSchriftarten
- GetSelectAnsprechpartner
- GetSelectUser
- GetStandardSteuersatzBefreit
- GetStatusAnfrage
- GetStatusAngebot
- GetStatusTicketSelect
- GetSteuersatzBefreit
- GetLager
- getFirstDayOfWeek
- GetFirmaBCC2
- GetEinkaufspreisStatistikWaehrung
- GetEinkaufspreisProduktionsartikel
- GetDatevKonten
- GetBundeslaender
- GetBondrucker
- getBacklink

## 22.3 Release and Patch Releases

### Patch Version 22.3.12

*Release date: 23-August-2022 *#### Bug fixes **Email accounts (TAN-2304)** The functionality to test an email configuration has been fixed. Clicking the buttontest connectionchecks whether the IMAP settings are correctly configured by sending a test mail. ** SuperSearch (TAN-2303)** The quick overview for addresses, documents, and products in the SuperSearch has been fixed. ** Purchase orders (FFU-820)**

Protocolsection in theProtocoltab is displayed again.

### Patch Version 22.3.11

*Release date: 11-August-2022 *#### Bug fixes **Amazon shopimporter (AMAZON-894)** Amazon orders were not imported. This has been fixed. ** Amazon shopimporter (AMAZON-900)** Provide characterization test for `Shopimporter_Amazon::amazonOrderToWaWi`** Amazon sales orders and invoices (FAC-767)**

Amazon sales orders and invoices were created with a wrong VAT tax rate (20.1%). This has been fixed.

### Patch version 22.3.10

*Release date: 10-August-2022 *#### Improvement **Delivery note (FFU-878)**

The query of the delivery note (Lieferschein) table has been optimized for better performance.

#### Bug fix **SuperSearch (TAN-2297)**

Due to an index error the SuperSearch did not work. This has been fixed.

### Patch Version 22.3.8

Release date: 09-August-2022

#### Improvements **Stock sync (ECOM-1349)** The performance of stock sync has been optimized. ** eBay (ECOM-1264)**

We have migrated from LMS API to the Feed API.

### Patch Version 22.3.7

*Release date: 27-July-2022 *#### New features **Chat (PIM-457)**

The chat feature is now available for users with access to a free trial instance. This way they can reach out to a sales engineer and immediately get help and additional information.

#### Improvements **Amazon API (Amazon-630)** Starting 31-July-2022 the MWS API calls for orders, reports and merchant fulfillment will no longer be available. ** Performance improvements**

We have implemented performance improvements in the Versanderzeugen module and improved the overall application performance across various modules.

### Patch Version 22.3.6

*Release date 19-July-2022 *#### Improvements **API (PIM-428)**

The /api/v1/dateien API endpoint now supports the upload of product images by adding the new parameters keyword_object (like "artikel"), keyword_subject, and keyword_parameter (id of product).

#### Bug fixes **Amazon (TAN-2200)** The 500 Error message no longer appears when importing orders from the intermediate table. ** Receipt importer (TAN-2164)**

The "NEW" variable now converts properly when importing a receipt from the new customer via the Belege import module (receipt import).

### Patch Version 22.3.5

*Release date 11-July-2022*

This patch includes minor bug fixes and further updates to the Amazon integration.

### Patch Version 22.3.4

*Release date: 6-July-2022 *#### Improvements **Performance improvement (TAN-2070)** General frontend improvements. ** Performance improvement (TAN-2142)**

We have improved the SystemSetting caching.

### Release Version 22.3

*Release date: 30-June-2022 *#### New features **Mollie integration**

You can now use Mollie as a payment provider in Xentral. This feature is available for users who are currently on the 22.1 version or newer. To learn more about this feature please check the[Mollie (Geschäftskonto)](https://help.xentral.com/hc/de/articles/5211449205532#UUID-f50a45d3-b649-65e4-144f-6fd697a52fcc).

#### Improvements **Amazon API updates ** We have added the option to select the new Selling Partner API integration. This is currently available only to the customers participating in the Beta program. To learn more about this please check the[Update der Amazon API](https://help.xentral.com/hc/de/articles/5223748428316#UUID-304257a3-92f1-bf94-639e-7c3f64ff1c6b)article. **Performance improvement (TAN-2068)** We have revised the table search filters to improve performance and usability. ** Performance improvement (TAN-2069)** We have revised the retrieval of the system basic settings for improved performance. ** Payment methods (FAC-1002)** We have added a check box that enables a new XML format for direct debit and transfers. To enable the new XML format, select thepain.001.001.03check box inAccounting>Business Accounts. ** Performance issue (TAN-2127)**

We have improved loading time when logging in as a non-admin user.

#### Bug Fixes

[en-us]**Sales orders (FFU-757)** We have fixed the quick column filters issue. They now return correct search results. ** Shopify (ECOM-1236)** The issue of sales orders that are not imported because of the missing first name in the customer address is now fixed. ** Shopify (ECOM-1142)**

Carrier_idenftifier no longer overwrites the carrier information from code.

## 22.1 Release and Patch Releases

### Patch Version 22.1.32

*Release date: 27-June-2022 *#### Improvements **Sales orders (FFU-757)**

Further usability improvement for the reset function of the column filter.

### Patch Version 22.1.31

*Release date: 22-June-2022*

#### Bug fixes

[en-us]**Sales orders (FFU-757)**

We have fixed the quick column filters issue. They now return correct search results.

### Patch Version 22.1.30

*Release date: 17-June-2022 *#### Bug fixes **Ticket System (TAN-1859)** We have fixed the issue with the missing date in the Ticket System module. ** WooCommerce (ECOM-798)**

We have fixed the type hit problem with the order import.

### Patch Version 22.1.29

*Release date: 16-June-2022*

#### Improvements

[en-us]**Payment methods (FAC-1002)**

We have added a check box that enables a new XML format for direct debit and transfers. To enable the new XML format, select thepain.001.001.03check box inAccounting>Business Accounts.

[en-us]**Performance improvement (TAN-2069)**

We have revised the retrieval of system basic settings for improved performance.

#### Bug fixes

[en-us]**Shopify (ECOM-1142)**

Carrier_idenftifier no longer overwrites the carrier information from code.

[en-us]**Shopify (ECOM-1236)** The issue of sales orders that are not imported because of the missing first name in the customer address is now fixed. ** WooCommerce (ECOM-798)**

Percentage discounts are no longer incorrectly taxed when importing to Xentral.

[en-us]**Performance improvement (TAN-2127)** We have fixed the performance issue that significantly reduced loading times when logging in as a non-admin user. ** Credit notes (FAC-813)**

We have fixed the issue where credit notes were no longer automatically offset against direct debits in payment notifications.

### Patch Version 22.1.28

*Release date: 08-June-2022*

#### Improvements

[en-us]**Performance improvement (TAN-2068)**

We have revised the table search filters to improve performance and usability.

### Patch Version 22.1.27

*Release date: 31-May-2022*

This patch includes a number of general enhancements in the background.

### Patch Version 22.1.26

*Release date: 27-May-2022 *#### Bug fixes **DHL 3.0 (FFU-445)** An issue with international shipments with DHL has been fixed. International return handling with Paket International works again. ** Shopify (ECOM-1153)**

An issue with pushing carrier information to Shopify has been fixed.

### Patch Version 22.1.25

*Release date: 17-May-2022 *#### Bug fixes **Ebay (ECOM-1122)** Fix for Ebay account deletion. Be aware that you must perform the following task: Please update the account deletion webhook URL in your Ebay account. ** Minor fixes with SQL**

This patch version contains a number of minor fixes with SQL.

### Patch Version 22.1.24

*Release date: 10-May-2022 *#### Improvement **Update process (TAN-2005)**

For all Xentral cloud customers, snapshots will be created directly before updates: This means that whenever you initiate an update, the app status before the update will be saved automatically and can be restored in case of any failures or problems during the update process.

### Patch Version 22.1.23

*Release date: 04-May-2022 *#### Improvement **Performance improvement (TAN-2031)**

We have removed duplicated indexes that were created with the 22.1 update. This will result in significantly less memory usage on your machine.

#### Bug fixes **Magento 2 (ECOM-1169)** In context with the sales order import from Magento2, there was an issue with the type return values. ** Shopify (ECOM-1163)** Issues (type return NULL) with the inventory sync to Shopify have been fixed. ** Shopify (ECOM-1130)** Due to a wrong standard template, smarty caused wrongly added line items to sales orders. ** Shopify (ECOM-1090)**

Issues with the standard smarty template for Shopify sales order imports have been fixed.

### Patch Version 22.1.22

*Release date: 26-April-2022 *#### Bug fixes **Document batch module (TAN-2006)** The document batch module did not work anymore. The invoice functionality for the document batch module has been fixed, so that the corresponding cron-job will work again properly. ** Profile picture upload (TAN-1983)**

The uploading of profile pictures did not work and has been fixed.

### Patch Version 22.1.21

*Release date: 21-April-2022 *#### Bug fix **Update process (TAN-2004)**

The stability of the update process to versions 22.1.xx has been improved.

### Release Version 22.1

*Release date: 20-April-2022 *#### New features **Mollie integration ** You can now use Mollie as a payment provider in Xentral. This feature is available for users who are currently on the 22.1 version or newer. To learn more about this feature please check the[Mollie (Geschäftskonto)](https://help.xentral.com/hc/de/articles/5211449205532#UUID-f50a45d3-b649-65e4-144f-6fd697a52fcc)article. **Snapshot before updates (TAN-1872)** For all cloud instances, once the update process has been triggered, a complete backup is created in the background prior to the actual update. ** Release notes (TAN-1761)** Display release notes in Xentral App: Before you actually update, you can view the release notes in the Xentral app to get an advance overview of all new features, improvements, and bug fixes. ** QuickBooks (FAC-186)** QuickBooks csv export: In the Reports module, there are 4 new standard reports available to generate CSV exports for QuickBooks for invoices, liabilities, credit notes and products. ** Xero (FAC-148)** Different filters on the invoices and credit notes for the Xero export: The customer can filter on the date by selecting a start and end date. ** Xero (FAC-147)** Manually adding invoices to an export queue ** Xero (FAC-146)** Create invoice/credit note Item mapping table for Xero accounts ** Xero (FAC-145)** Xero integration global or custom mapping ** Xero (FAC-144)** Link the Xero account to Xentral: You can now connect your Xero account to Xentral by adding the Client ID and the Secret ID ( provided by Xero) in Xentral. ** GUI (GTM-60)** Add module overview page ** Queue system (TAN-35)**

Queue System: Xentral 22.1 comes with a queue component to normalize workloads. The queued jobs are executed by a long running worker process.

#### Improvements **PHP (TAN-1932)** PHP readline extension: We removed the readline PHP extension as a prerequisite for 22.1 Xentral updates. ** Update process (TAN-1682)** Update process only starts if minimum PHP requirements are met: The update process will only start if the minimum requirements (PHP version, extensions) are met in order to avoid that Xentral does not function properly anymore after an update due to missed server requirements. ** Placetel (TAN-1585)** Update Placetel API to v2: The Placetel integration shifts consumption from depreciated v1 to the new v2 API provided by the vendor. This does not change any functionality within the integration. ** Search (TAN-1436)** Show module description in super search & link to help space: In order to keep our documentation synchronous and up-to-date we have have added module descriptions to the super search results and also link out to the latest documentation in our help space. ** Welcome screen (GTM-470)** Link attached to Help icon in welcome screen: Was directing to a 404 page. Now directs users to Implementation guide. ** Welcome screen (GTM-469)** Handling Javascript exceptions on welcome page ** Localization (GTM-468)** English translation in module artikelforecast: For creation of a new product, Save and Cancel buttons have been translated. For the deletion of an existing entry, the Delete pop up has been translated. ** Localization (GTM-419)** All modal buttons have been translated to English ** Updates (TAN-1034)** Use.env migration in update process ** Currencies (FAC-430)** Add currency-information in contact-receipt site ** Currencies (FAC-426)** Adding a Currency Column in the Dunning System List ** Localization (GTM-407)** English Translations: Missing translation in Master data and Shipping center modules are addressed ** Localization (TAN-783)** Added $linkType flag to \erpAPI::MenuEintrag(): \erpAPI::MenuEintrag() received a new $linkType parameter that specifies how the link should be displayed ** Datev (FAC-175)** Oauth refresh token is used for authentication for Datev Export ** Localization (TAN-638)** Localized help can be accessed through question mark now: The handbook now opens in a new tab in the right language (EN or DE) and is accessible through the question mark icon in the upper right-hand corner ** Projects (FAC-170)** Ability to exclude projects from being subject to Lieferschwelle App ** GUI (MIRAI-214)** Style update throughout the UI (including buttons colors, hover effects, icon style...)** Localization (GTM-148)** Pdf translations ** Localization (GTM-146)** PDFs are translated to English: This has been done for the following modules: Fulfillment > Inventory, Fulfillment > Minimum stock quantities, Team > Employee time recording, Sales > POS, Purchasing > Price inquiry ** Localization (GTM-145)** Translation of pdfs ** Localization (GTM-143)** Translation of pdfs ** Datev (FAC-142)** Improved upload behavior for DATEV interface.: Large file sizes and big number of invoices often posed problems when uploading to DATEV. The interface now allows for partial uploads which will resolve most of the performance issues with regards to DATEV. ** GUI (TAN-393)** Error screen has been improved ** Users (GTM-116)** Create User - Optimize UX of user creation ** OSS (FAC-6)** Country ISO code "UK" has been removed from laender table: This change will only come into effect for new instances ** Kaufland (ECOM-383)** Rename 'real.de' to 'Kaufland': Renaming of front- and backend from real.de to Kaufland. ** GUI (GTM-76)** Navigation refactoring ** Datev (FAC-45)** DATEV xml validation showing user friendly error message ** Datev (FAC-88)** Option to export only unexported documents: It is now possible to only export documents for Datev XML & Datev CSV export that have not been exported previously ** Dashboard (GTM-6)** Improve Dashboard for better onboarding ** Shopware 6 (ECOM-203)** Shopware6 transfer dimensions for variants: Enabling of the transfer of dimensions for variants to Shopware6 ** Shopware 6 (ECOM-200)** Shopware6 transfer manufacturer for variants: Exporting of manufacturer to Shopware6 is enabled for variant products. ** Shopware 6 (ECOM-201)**

Shopware6 transfer meta information for variants: Enabling of the transfer of meta information for variants to Shopware6

#### Bug fixes **Sales order (TAN-1958)** There was a CSRF token mismatch when downloading collect PDF from spooler after update. ** Addresses (TAN-1950)** There was a CSRF token mismatch resulting in an error 419 when trying to attach a file to an email in the CRM area of an address. ** Articles (TAN-1944)** There was a CSRF token mismatch in the article batch processing. ** Employee time tracking (TAN-1617)** There were multiple emails sent for vacation requests. ** Phone callback (TAN-1935)** Phone callback records were duplicated: When you created a phone callback record it appeared as duplicated entry. ** Employee time recording (TAN-1934)** The employee time recording module could not be activated. ** Favorites (TAN-1813)** The bookmarks on the Welcome page could not be edited. ** Addresses (TAN-1809)** Magnifying glass icon did not filter. ** Sales order (TAN-1725)** Contribution margin was not displayed: In sales orders, the contribution margin will now appear in the Details dialog box. ** Payment methods (FAC-848)** Module did not work in Beta Patch 22.1.15; this has been fixed now. ** Hubspot (TAN-1653**)

Error message when trying to activate the groups in an address **Xentral Boss app (TAN-1550)** Connection to Xentral Boss app was not possible. ** Spooler (TAN-1695)** Printed label not set on printed invoices ** Products (TAN-1839)** Double click on "Create Product" creates 2 identical products. ** Backup (TAN-1805)** Backup module not working: Due to a cronjob error the backup feature did not work accordingly. ** Placetel (TAN-1758)** Outgoing and incoming calls do not work with Placetel: We adjusted our integration to work with Placetel 2.0 API. You are now able to use Xentral in combination with native Placetel App for incoming and outgoing calls. ** Time tracking template (TAN-1663)** The New button redirected you to the welcome page instead of allowing you to create a new time tracking pattern. ** Liabilities (FAC-633)** Supplier is blank on saving the liability that is created from invoice ** Parts list (TAN-1464)** Parts list is not refreshed: When you are changing the amount of an article within a parts list (JIT) using the pencil button, the parts list including the receipt was not refreshed accordingly. ** Store delivery (FFU-228)** A partial shipment to a store is not shown in "store delivery". ** Liabilities (FAC-729)** Filter is shown correctly again ** Ticket system (TAN-1799)** Responses to tickets are not sent to customer: Once you answer a ticket, the response will now be send to the ticket owner (customer) and not to the assignee of the ticket anymore. ** API (TAN-1747)** AuftragCreate ignored the project for existing customers ** Total discounts/sales order (TAN-1734)** Popup for total discount appears again in sales order ** API (TAN-1791)** API endpoints were not working. Requests to our API endpoints were fixed. ** Shopify importer (ECOM-1055)** Information about manufacturer was not transferred. ** Login (TAN-1558)** Simultaneous login from different browser: As soon as you start a new session in Xentral, e.g. log in from a different location or browser, your old session will automatically expire and a new login is requested. This has been implemented to secure your session. ** Production (FFU-420)** Action buttons are working again. ** Production (TAN-1645)** Customer can be added to production again. ** Picking Process (FFU-425)** Problems with booking out articles in the 2-step picking process have been resolved. ** Invoices (FAC-805)** Action buttons are working again. ** Orders (FFU-351)** Adding a supplier to a purchase order is possible again. ** WooCommerce (ECOM-1013)** Fix product status issues with the WooCommerce shop importer: This fix provides a solution for the issue that products were set to 'inactive'. ** Documents (TAN-1703)** Subject line in documents not visible: Indeed, the subject line had been there all the time, however with a font size of 1. This has been corrected by increasing the attribute to an appropriate size. ** Projects (TAN-1629)** Project Module: Link to navigate to follow up screen is broken ** Invoice (TAN-1628)** Invoices can not be continued as credit notes: The bug is fixed, on an invoice you may select from the dropdown menu the action "as a credit / Stornorechnung" and the selected action will take place. ** Contacts (TAN-1594)** Creating a contact person without admin-rights cause error: As a user without admin-rights you will now be able to successfully edit a contact person. ** Login (TAN-1558)** Simultaneous login from different browser: As soon as you start a new Session in Xentral, e.g. log in from a different location or browser, your old session will automatically expire and a new login is requested. This has been implemented to secure your session. ** Purchase order (TAN-1547)** Purchase Orders: Fields are not disabled in read-only mode: Once a purchase order is set to read-only mode, the corresponding fields become grayed out. ** Controlling (TAN-1542)** Controlling-Module: Sales figures and stats are duplicated: We have fixed the duplication of graphs and statistics in the sales figures area. ** Products (TAN-1525)** API: Create Articles overwrite scaled prices: If your request does not include any scaled price [staffelpreis] attributes, the request will not overwrite any scaled prices that had been set in the past. ** Templates (TAN-1458)** Creation of new template stops function of +new button of several modules ** Emails (TAN-1448)** New email field data migration does not respect unique index on user.email ** Sales orders (TAN-1402)** Sales Order: No records are displayed under delivery handover in sales order ** Tickets (TAN-1371)** Time is not shown correctly in a ticket ** Vouchers (TAN-1350)** Vouchers: unable to view the vouchers generated and unable to create vouchers ** Updates (TAN-1317)** Fixed issues with errors during updates ** Login (TAN-1315)** Fixed issues with loading of login page ** Datev (FAC-590)** Datev Export Will Now Accept Special Characters in Invoice Number ** Login (TAN-1261)** User: Login for admin users fails after a while ** Tickets (TAN-1254)** Ticketing System: Empty tables when assigning attachments ** Taxdoo (FAC-552)** Fixing the missing orders on Taxdoo ** Projects (TAN-1238)** Project module: Generating CSV/ PDF files from the project dashboard is not working ** Sales orders (GTM-441)** Sales Order(Positions Tab): A new template section is added under the positions tab in sales order module ** Sales orders (TAN-1229)** Sales Order: price doesn't get recalculated ** Projects (TAN-1228)** Project: Adding a NEW Article/Product within the Project module not possible ** Projects (TAN-1227)** Project: Adding existing Product leads to insert of new Xentral interface within Module ** Export (TAN-1219)** Tables: Excel Export not available anymore ** Localization (GTM-426)** Fix loading Lang.js and setting locale order ** Core (TAN-1187)** Fixes for multiple Javascript errors ** Invoice (FAC-522)** Belegeimport Module can multiply Position Entries on Invoice during import ** Invoice (TAN-1184)** Minidetail not shown in "invoices not sent"** Shipping (TAN-1144)** Versanderzeugen: Table empty after initial access of module ** Userlane (GTM-410)** Userlane Snippet not available ** Free text (TAN-1132)** Possibility to add free fields to PDF of picking list ** Products (TAN-1131)** Sorting of uploaded files changed fixed ** Products (TAN-1122)** Articles: no possibility to click Save Button in certain circumstances ** Sales orders (TAN-1120)** Auftrag: canceled productions are shown wrong ** Master data (TAN-1118)** Copy existing project redirects to an empty page ** Search (TAN-1113)** SuperSearch: Opening delivery notes by using the super search leads to errors ** User rights (TAN-1109)** User: Refresh after setting all rights for one module ** Matrix products (ECOM-670)** Matrix product: ID of first variant is automatically added to article number ** Welcome screen (TAN-1107)** Welcome Screen: individual starting page is ignored ** Credit notes (GTM-398)** Module: Credit Note-Refund Payment option should be removed from credit note screen for US version ** Invoice (GTM-397)** Module Invoice (US): Invoice to Liability option should be removed from actions dropdown ** Products (GTM-390)** Products: spelling in purchasing price ** Shopware 5 (ECOM-666)** Shopware 5: Exporting group prices is not possible ** Localization (GTM-384)** Purchase order: English title in german version ** Products (GTM-385)** Products/GUI: Wrong tab title in products overview ** Products (TAN-1086)** Article: minidetail/description HTML not masked ** Documents (TAN-1073)**"show product attachments" is missing when submitting documents ** Purchase order (TAN-1071)**Purchase Order: Notice regarding archiving or sending purchase order missing ** Chat (TAN-1065)**Chat: Counter for unread messages although all messages are read ** GUI (GTM-386)**Frontpage/GUI: inconsistent spacing in menu bar ** Delivery note (TAN-1052)**Lieferschein - PDF functions not working for the tabs - Bewegung & Datei ** Localization (GTM-379)**Missing translation in?module=auftrag&action=list Filter Status Select ** GUI (GTM-393)**Scrolling in table views ** Products (TAN-1037)**Article Creation via xml and "Übertragungen" Module not possible ** GUI (TAN-1199)**Improved date and time formatting: We improved date and time functions that are used internally in the application. This can lead to slightly different date and time formats. ** Contacts (TAN-1031)** New addresses can not be set up with a role in certain circumstances **Order proposal (TAN-1032)** Bestellvorschlag: Months are not shown correctly **Production (TAN-1001)** MySQL error on creation of new production & assigning a customer **Calendar (GTM-392)** no calender view in "lieferdatum" in article in order **Sales orders (GTM-373)** Add correct link to handbook page on Sales Order > Delivery Handover **Calendar (TAN-975)** Calendar module disappeared from the welcome screen menu bar **Userlane (GTM-358)** Fix Userlane for US **Products (TAN-998)** Product module: adding purchasing price for a product shows a broken tax calculator **Tickets (GTM-324)** Improve translations for ticket module **Offers (GTM-317)** Module:Offers (US) -The default value displayed for currency and language is incorrect **Netstock (TAN-889)** Netstock - wrong email is imported within "Bestellungen"** GUI (GTM-280)** Status Message "SHARE" isn't valid **Localization (GTM-262)** Data Import Translations target dropdown contains "nbsp" (Backspace) code **TSE (FAC-373)** Error fixed when trying to set up TSE (Fiskaly)** Credit notes (TAN-804)** Internet number is not shown in protocol of credit note. ** Datev (FAC-366)** CSV Export for Datev has wrong formats/data **Localization (GTM-239)** The currency and the language is not configured to US settings by default in Purchasing and sales orders **Contacts (GTM-238)** Addresses (Translation Not Complete) Value "Folgebestätigungsperre:"** Reports (TAN-766)** Layout error in Reports module fixed **Liabilities (TAN-791)** Liabilities are not loaded or displayed to "Zahlungsverkehr"** Bulletin board (TAN-718)** Some dialog boxes displayed some resizing problems in the UI. ** Pipedrive (TAN-669)** Pipedrive does not sync and error message does not disappear **Localization (GTM-188)** Missing translations for "calendar"** Localization (GTM-173)** Missing translations for "tickets"** Pipedrive (TAN-621)** pipedrive_process processstarter missing in 21.1 ** Products (TAN-571)** Delete article leaves foreign numbers in the database. ** Sales orders (TAN-468)** Pagination broken in List View in Order Overview **Tasks (TAN-412)** Tasks module History mixed up on different Tasks **Shopware 6 (ECOM-258)** Shopware6 Import correct PayPal TransaktionID: We implemented a routine to get ‘transactionNumber‘ from the first used payment we detect. ** Magento 2 (ECOM-185)** Free text not transferred from Magento 2 ** Magento 2 (ECOM-174)** Magento 2.x: Sorting order of images and store view are ignored **Liabilities (FAC-392)** Partially paid liabilities do not appear in payment transactions **Shopware 6 (ECOM-114)** Shopware6 Transfer Online-Shop-Texte and Artikelnamen for variants: Enabling of the transfer of 'Online-Shop-Texte' and 'Artikelnamen' for variants to Shopware6 ** Shopware 6 (ECOM-156)** Shopware 6: Product item export fails if meta description has more than 255 characters **Shopware 6 (ECOM-134)** Shopware 6: Transfer translation of matrix variant properties **Datev (FAC-80)** Datev export: invoices with file size of > 20MB cannot be exported: A restriction of the DATEV API is that only invoice PDFs with less than 20MB can be imported. For invoices pdfs with more than 20MB an error message will be now shown upon export. ** Presta shop (ECOM-129)** Presta shop: Weight not correctly added to product, but shown additionally as property **Presta shop (ECOM-128)** Presta shop: Tax not properly transferred **Presta shop (ECOM-127)** Presta shop: Variants and properties exported incorrectly **Presta shop (ECOM-126)**

Presta shop: Wrong category links

#### Removals **Onboarding steps on Welcome screen (TNG-77)** The onboarding steps box on the Welcome screen has been removed as part of a general overhaul of our onboarding experience. ** Project label in app store (TAN-1878)** The Project label that used to be attached to some apps in the app store has been removed because showing this label does not add any value to the user. ** Copper surcharge (TAN-1110)** Copper surcharge module has been removed ** Oberflächen Übersetzung (TAN-799)** Module "Oberflächen Übersetzung" has been removed ** Pygen (TAN-324)** pygen has been removed ** ELO (TAN-276)** Module ELO DMS Archiv has been removed ** Netzwerk (TAN-275)** Module Netzwerk has been removed ** Patagona (TAN-274)** Module Patagona has been removed ** Mobile (TAN-273)** Module Mobile has been removed ** Vorlage (TAN-272)** Module Vorlage has been removed ** Linkeditor (TAN-271)** Module LinkEditor has been removed ** Terminal (TAN-270)** Module Terminal has been removed ** Servicetools (TAN-269)** Module Servicetools has been removed ** Inhalt (TAN-267)** Module Inhalt has been removed ** Geraete (TAN-266)** Module Geräte has been removed ** Einkaufabgleich (TAN-264)** Module Einkaufabgleich has been removed ** Demodaten (TAN-263)** Module Demodaten has been removed ** Snapaddy (TAN-262)** Module snapaddy has been removed ** WawisionOTP (TAN-260)** Module Wawision OTP has been removed ** GoogleAPIPrint (TAN-216)** GoogleAPIPrint has been removed ** ReconnectUser (TAN-112)** reconnectUser from BackupService has been removed ** Web-triggered cronjob (TAN-108)** Web-triggered cronjob has been removed ** Loqate (TAN-106)** Module Loqate has been removed ** GobNav (TAN-92)** Module GOB Navision Connect has been removed ** RealSMS (TAN-91)** Module RealSMS has been removed ** Supportbackend (TAN-89)** Module supportbackend has been removed ** Supportapp (TAN-87)** Module supportapp has been removed ** Themes (TAN-85)** Possibility to define custom colors or themes has been removed ** MultiDB (TAN-83)**

Module MultiDB has been removed