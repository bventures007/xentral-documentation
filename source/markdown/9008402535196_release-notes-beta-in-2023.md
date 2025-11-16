> **Tipp**
>
> Dies ist ein separater Artikel, um Release Notes für Kunden aufzulisten, die imBeta Programmsind.
>
> Falls du kein Teil des Beta-Programms bist, findest du die aktuellen Release Notes für dich hier:Release Notes von 2023

> **Anmerkung**
>
> Updates von einer XentralVersion 21.x oder älter auf die aktuellste XentralVersion können eine längere Zeit in Anspruch nehmen - abhängig von der Menge an Daten in deiner XentralInstanz. Bitte habe etwas Geduld.

## 23.26 Release and Patch Releases

### Patch Version 23.26.10

*Release date: 03-January-2024 *#### Bug fix **Sales order (FFU-2804)**

Resolved an issue that occured when importing sales orders via API.

### Patch Version 23.26.9

*Release date: 22-December-2023 *#### New feature **Mobile Inventory App (FFU-2469)**

A new inventory app, which allows you to count your stock using multiple mobile devices at the same time, is now available to beta customers who have joined the early access program of this app.

### Patch Version 23.26.4

*Release date: 15-December-2023 *#### Bug fix **Kaufland (ECOM-3974)**

Order imports can now accurately identify external products in Xentral using their EANs.

### Patch Version 23.26.3

*Release date: 14-December-2023 *#### Bug fix **Item tree (PIM-1870)**

Resolved an issue where the item tree displayed deleted categories. All entries in the item tree are now displayed correctly.

### Patch Version 23.26.2

*Release date: 14-December-2023 *#### Bug fixes **Inventory performance (XIN-781)** The table in the Inventory Performance module now displays the correct data for the 'average retail value' column. ** Inventory performance (XIN-778)**

The table in the Inventory Performance module now has the 'Inventory Value' column correctly formatted as a currency, and the missing 'Total Quantity' column is now visible.

### Patch Version 23.26.1

*Release date: 12-December-2023 *#### Bug fix **Transfers (FFU-2731)**

Resolved an issue where the process starter "api_uebertragen" stopped working when trying to create a PDF with an invalid template.

### Release Version 23.26.0

*Release date: 12-December-2023 *#### Improvements **Update Button (TAN-4109)** Admins of non-beta instances will find an update button in the navbar whenever a new version is available. ** Settings (TAN-4032)** Project views within settings have been enhanced for a better user experience. ** Settings (TAN-4026)** The "Advanced settings" toggle has been removed. All settings are now enabled or disabled based on license information. ** Products (PIM-1460)** In the Products module, free fields can now be filtered using the search field. ** Warehouse API (FFU-2530)** An endpoint has been implemented to retrieve items located in a storage location. ** Invoice API (FAC-2753)** The List Invoices API endpoint now includes the possibility of filtering by the ID of the connected sales order. ** Amazon VCS (ECOM-3853)**

The VCS invoice import will now select the most accurate tax rate for the invoice's country to prevent discrepancies in the calculated tax rate, as long as the "Steuersätze" module is filled with accurate data.

#### Bug fixes **Report (TAN-4123)** Comma and escaping issues in CSV exports in the Report module have been resolved. ** Product (PIM-1588)** Resolved an issue with the processing of text fields in shops when using bulk processing. ** Transfers (FFU-2737)** SFTP private key authentication with passphrase is working again. ** Process starter (FFU-2723)** The folgebestaetigung process starter now correctly sends emails only for sales orders with an activated project setting. ** Post.AT (FFU-2709)** The printer from the user settings will now be used if the printer field in the Post.AT shipping method is left empty. ** GLS (FFU-2692)** The tracking links for GLS were not working. This has been fixed. ** Sales order (FFU-2613)** In the sales order list view, actions in the mini detail were occasionally applied to the incorrect sales order when multiple sales orders were expanded. This has been fixed. ** Dispatch center (FFU-1940)** The serial number wizard in the dispatch center is now working again. ** DATEV (FAC-2737)** Amounts in grouped positions of invoices and credit notes get calculated correctly, when the first position is a discount. ** Financial accounting export (FAC-2705)** Tax rate is now properly exported in the Financial Accounting Export for liabilities. ** Cost center (FAC-2682)** Cost centers with more than 10 characters can now be used in the Invoice and respective Accounting exports. ** Amazon (ECOM-3952)**

Fixed an issue where "Artikel anhängen" created numerous incorrect entries in the "amazon_merchantgroup" table.

#### Removal **Amazon MFN (ECOM-3956)**

Support for Amazon's MFN via our Transfer Module, previously facilitated by the Amazon MWS API, has been discontinued.

## 23.25 Release and Patch Releases

### Patch Version 23.25.3

*Release date: 06-December-2023 *#### Bug fix **Amazon VCS (ECOM-3972)**

Resolved an issue where promotional discounts were not correctly included in invoices and credit notes from Amazon VCS.

### Patch Version 23.25.2

*Release date: 05-December-2023 *#### Bug fix **Dropshipping Warehouse (FFU-2496)**

New options have been added to the Dropshipping Warehouse that improve the logic for how sales orders are processed.

### Release Version 23.25.1

*Release date: 05-December-2023 *#### Improvements **User (PF-2023)** Users can now be invited more easily, by only adding a name and email, while the related "Contact" can be automatically created and connected in the background. ** Warehouse API (FFU-2636)** If there is no project linked to a warehouse, the endpoint now returns project: NULL instead of a project object with ID = 0. ** Shipping method: Address label (FFU-2633)** The shipping method "Address label" is now available in all licenses again. ** UPS OAuth (FFU-2629)**

UPS will now receive phone + email address provided the GDPR settings are set to allow transferring customer details to shipping carriers.

NOTE: This fix is ONLY applied to the new UPS (OAuth) shipping method. We recommend all users to migrate to the new UPS (OAuth) shipping method.

**Process starter (FFU-2602)** The process starter configuration now displays immediate warnings in case the execution frequency is shorter than allowed. ** DATEV Connect Online (FAC-2576)** Improved the performance of the DATEV Connect Online export. ** Amazon (ECOM-3876)** FBA orders can be configured to be created with a 24h delay. This will improve the handling of differing billing addresses. ** Navbar (TAN-3973)**

New Sales Channels can be accessed.

#### Bug fixes **Follow-up (TAN-4079)** Enhanced performance in displaying Stage-view for Follow-ups. ** Layout template attachment (TAN-4054)** Improved error handling in PDF creation. ** Follow-Up (TAN-3041)** Follow-Ups are now correctly displayed in all stages that are set to be shown. ** NextGen product table (PIM-1788)** Retaining search field entries when returning from product details to NextGen product table view. ** Protocol (PF-1876)** Resolved issue of missing dates in the protocol overview of sales orders following changes in user settings. ** Netstock (FFU-2703)** Resolved issues with saving SQL statements in the Netstock module. ** Delivery note (FFU-2698)** Fixed the PDF previews for delivery notes that have no tracking numbers. ** Return Reasons API (FFU-2611)** Return Reasons API was requiring a project ID which is an optional parameter. This has been fixed so that the full list of return reasons can be obtained without specifying any project ID. ** DPD (FFU-2554)** Resolved an issue where the {TRACKINGNUMMER} variable did not display all tracking numbers for delivery notes with multiple entries. ** Dropshipping supplier (FFU-2022)** Corrected an issue where fixed-value discounts were duplicated in split orders. Now, only percentage discounts are copied, while fixed-value discounts stay on the main order. ** Delivery note (FFU-1898)** The quick preview and protocol of delivery notes created for suppliers were displayed incorrectly. This has been fixed. ** Taxdoo (FAC-2742)** Saving Taxdoo configurations with single quotes no longer results in added backslashes. ** Liabilities (FAC-2741)** Adjusted liability tax configurations to prevent the addition of slashes when using single quotes. ** Financial accounting export (FAC-2710)** Resolved an error occurring with 0.00 amount credit notes during export. ** DATEV Company Online (FAC-2706)** In DATEV Company Online, the costCategoryId field will now correctly show the assigned cost center. ** POS (FAC-2669)** For the new POS, the GET Journal List endpoint will now be properly filterable by salesOrderId and externalOrderNumber. ** DATEV Connect Online (FAC-2625)** Documents, which are exported via Datev XML file export, are no longer excluded in Datev Connect Online. ** Amazon Seller App (ECOM-3885)** In-transit stock quantity is set to 0 upon reaching its destination. ** Amazon (ECOM-3867)**

The Amazon shopimporter is now accessible even when all marketplace IDs are disabled.

## 23.24 Release and Patch Releases

### Patch Version 23.24.6

*Release date: 29-November-2023 *#### Bug fixes **PayPal (FAC-2731)** Import of PayPal fees now requires a default cost center or revenue account to be set. ** POS (FAC-2727)**

When creating a credit note via API from a return, and it's marked as approved, the document number is now correctly populated.

### Patch Version 23.24.5

*Release date: 24-November-2023 *#### Bug fixes **Paypal (FAC-2536)** Fees associated with PayPal refunds are now accurately imported as debits during the import process. ** Billbee (ECOM-3929)**

An issue with handling incorrect responses from Billbee has been fixed.

### Patch Version 23.24.4

*Release date: 21-November-2023*

This version fixes several issues regarding PHP 8.1 compatibility.

### Patch Version 23.24.3

*Release date: 20-November-2023*

This version fixes several issues regarding PHP 8.1 compatibility.

### Patch Version 23.24.2

*Release date: 16-November-2023 *#### Improvement **Financial accounting export (FAC-2614)**

Any errors that occur during the CSV export are now collected into a separate log file that is exported together with the CSV output.

#### Bug fixes **Product (PIM-1774)** Resolved a PHP 8.1 error that occurred when importing a bill of materials for a product. ** Receipt of payment (FAC-2619)** Resolved an issue where Shopify payment transactions were imported twice, but with different names. All Shopify payments are now correctly imported only once. ** Batches (FFU-2140)**

Batches (pick list profiles) processing sometimes left sales orders unprocessed. This has been fixed.

### Patch Version 23.24.1

*Release date: 15-November-2023 *#### Improvement **DHL (FFU-2608)**

Added a check box to the DHL shipping method that allows you to exclude the components of a JIT (Just in time) bill of materials on the CN22 customs form.

### Release Version 23.24.0

*Release date: 14-November-2023 *#### Improvements **Service account (PF-2009)** Removed the green notification dot from the service account menu item to reduce confusion among users. ** Xentral UI (PF-2005)** Updated display to show the correct plan for users' instances and a badge indicating participation in the beta program. ** Delivery notes API (FFU-2527)** Launched the Delivery notes VIEW endpoint. ** Warehouse API (FFU-2455)** Implemented an endpoint for retrieving a list of all storage locations in a warehouse. ** Sales order API (FFU-2361)**

Enhanced functionality to allow the import of dedicated discounts for sales orders.

#### Bug fixes **NextGen Navbar (PIM-1789)** Modules Employees, Calendar, and Production Center now show up in the side navigation when selected in the user preferences. ** Batches (FFU-2378)** Resolved an issue where canceling delivery notes resulted in double batches. ** Returns (FFU-1997)** The debitor value is now correctly filled on the credit note when created from a return document. ** Shipping tax split (FAC-2638)** The shipping tax split logic is no longer applied when an order is split into partial orders or it is itself a partial order. ** DATEV Connect online (FAC-2625)** Documents, which are exported via Datev XML file export, are no longer excluded in Datev Connect Online. ** Shipping tax split (FAC-2188)**

Ensured accurate import of shipping costs in sales orders and invoices when the shopping cart contains only free products.

## 23.23 Release and Patch Releases

### Patch Version 23.23.5

*Release date: 10-November-2023 *#### Bug fix **eBay (ECOM-3905)**

Due to issues with the ebay_bulkjobs process starter, the stock sync with eBay was not working. This issue has been fixed.

### Patch Version 23.23.4

*Release date: 10-November-2023 *#### Bug fix **eBay (ECOM-3903)**

Resolved an issue with the eBay user shop token.

### Patch Version 23.23.3

*Release date: 09-November-2023 *#### Bug fix **Transfers (FFU-2582)**

Files could not be downloaded from SFTP servers due to issues with file paths. This issue has been fixed.

### Release Version 23.23.0

*Release date: 07-November-2023 *#### Improvements **Contacts (TAN-3713)** When a user creates a new contact with the role employee, that new employee gets access to the same projects as the user creating the contact. ** Process starter (FFU-115)** The process starter configuration now displays a warning for periodic process starters with periods set below the allowed minimum. ** DATEV (FAC-2607)** When a PDF is not found in the archive for DATEV Unternehmen Online and DATEV Connect Online, it will be generated automatically. ** DATEV Connect Online (FAC-2600)** The export history is now shown for DATEV Connect Online. ** DATEV Connect Online (FAC-2581)** In any DATEV XML export, the articles are now also grouped by cost centers. ** Financial accounting export (FAC-2495)** Date ranges for previously exported documents are now displayed in the Financial Accounting Export. ** Amazon (ECOM-3814)**

Amazon order import will fetch the VAT ID if a buyer has one.

#### Bug fixes **Transfers (FFU-2572)** Empty SFTP ports will now fall back on the default port 22. ** DHL Express (FFU-2568)** An exception was caused whenever the country settings were empty. This issue has been fixed. ** Post AT (FFU-2564)** Resolved an HTTP 500 error when scanning a parcel from Post AT. ** Swiss QR Invoice (FAC-2621)** The Swiss QR Invoice Module is now findable in the appstore and the search bar. ** Receipt of payment (FAC-2603)**

The transactions in PayPal are checked for doublets independently from the misleading customer/business name.

## 23.22 Release and Patch Releases

### Patch Version 23.22.3

*Release date: 06-November-2023 *#### Bug fix **DPD (FFU-2542)**

DPD shipping labels with a shipping date on weekends or bank holidays could not be created anymore. There is now a new setting in the DPD shipping method that allows you to automatically set the shipping date to the next business day.

### Patch Version 23.22.2

*Release date: 06-November-2023 *#### Bug fix **Overview Dashboard (XIN-697)**

Product SKUs were not showing on the Overview Dashboard, but are now visible again.

### Patch Version 23.22.1

*Release date: 01-November-2023 *#### Bug fix **Amazon (ECOM-3863)**

An issue with the transmission of tracking information and shipment numbers from Xentral to Amazon has been fixed.

### Release Version 23.22.0

*Release date: 31-October-2023 *#### Improvements **NextGen Navbar (TAN-3909)** The navigation has been improved to reduce mouse travel time. ** NextGen System Messages (PIM-1752)** A badge indicating system message count has been added to the user avatar in the navigation sidebar. ** User Settings (PF-1969)** Updating your email address will now log you out to ensure you can login with the new email. This change will also update the login email in other instances using the same address. ** Return Reasons API (FFU-2548)** Switched return reason IDs from UUID to auto-increment. ** Deliveries API (FFU-2464)** Added tracking link and carrier name to the payload of the LIST endpoint. Note: Currently not functional for Sendcloud. ** Deliveries API (FFU-2425)** Tracking information has been added to the delivery note LIST endpoint. ** Sales Order API (FFU-2424)** Sales Order Import API now allows importing of shipping costs via a separate parameter object. ** Sales Order API (FFU-2384)** Added effectiveVat to the tax object in positions of the sales order VIEW endpoint. ** Transfers (FFU-2377)** SFTP has been fixed so that modern encryptions are now supported. ** POS API (FAC-2577)**

The GET Journal List endpoint now also contains and can be filtered by the externalOrderNumber field.

#### Bug fixes **Protocol (PF-1876)** Resolved issue of missing dates in the protocol overview of sales orders following changes in user settings. ** DPD (FFU-2381)** Tracking numbers were not stored in the invoice when 'complete immediately' is activated in DPD shipping method. This has been fixed. ** Transfers (FFU-1915)** Resolved existing issues related to SFTP and folder interactions. ** Mollie (FAC-2606)** Fixed an error that occurred when the state request parameter was missing. ** DATEV Unternehmen (FAC-2599)** In DATEV Unternehmen exports, zero-amount invoices are now properly ignored regardless of the setting to include them in the CSV export. ** Financial accounting export (FAC-2594)** In Column N, product details will now be displayed when grouped by product. ** Financial accounting export (FAC-2589)** Resolved an issue where the export would fail with a value of 0.00. ** Financial accounting export (FAC-2588)** The account period saved in the settings is now displayed correctly in the financial export CSV files. ** Financial accounting export (FAC-2546)** When exporting accounts, accounts will now be sorted by account id and transaction date. ** Financial accounting export (FAC-2538)** XML consolidatedAmount will now properly match with the sum of the positions. ** Financial accounting export (FAC-2537)** Negative liabilities are now displayed correctly in the DATEV XML exports. ** Process starter (ECOM-3823)** Resolved an issue where successful cronjob runs were not displayed if below a certain threshold. ** Shopware 6 (ECOM-3375)**

Products with a price of 0 are now correctly imported and displayed as expected.

## 23.21 Release and Patch Releases

### Patch Version 23.21.3

*Release date: 25-October-2023 *#### Bug fix **Revenue Analyzer (XIN-678)**

An issue with the columns in the Revenue Analyzer table has been fixed.

### Patch Version 23.21.2

*Release date: 25-October-2023 *#### Bug fix **Receipt of Payment (FAC-2560)**

An issue where selecting the "Complete Bookings" button in Incoming Payments module was producing a 500 error has been fixed.

### Patch Version 23.21.1

*Release date: 24-October-2023 *#### Bug fix **Export template (TAN-3943)**

The CSV export in the Export templates module now correctly interprets special characters.

### Release Version 23.21.0

*Release date: 24-October-2023 *#### New feature **Revenue Analyzer**

Exclusive to NextGen design, the Revenue Analyzer allows you to analyse your sales order and invoice based revenue by drilling down to the product, sales channel or project level. Try it now and give us your feedback at analytics[at]xentral.com!

#### Improvements **Products API (PIM-1567)** Added the "thumbnailId" property. ** Deliveries API (FFU-2425)** Tracking information has been added to the list endpoint. ** Warehouse API (FFU-2382)**

Introduced an endpoint to retrieve all available warehouses in an instance.

#### Bug fix **Dispatch center (FFU-2483)** The validation for allowed product numbers when scanning items in the dispatch center was not working correctly, resulting in a page load & delayed warning when scanning an incorrect item. This has been fixed. ** Financial accounting export (FAC-2505)** The ContraAccount property type has been changed from "integer" to "string" to prevent conversion to "0". ** Invoice (FAC-2499)**

Corrected the cash discount calculation in the protocol.

## 23.20 Release and Patch Releases

### Patch Version 23.20.7

*Release date: 23-October-2023 *#### Bug fix **Swiss QR invoice (FAC-2569)**

Invoices in draft mode no longer throw errors in the PDF preview if the Swiss QR Invoice module is active.

### Patch Version 23.20.6

*Release date: 20-October-2023*

This version contains preparations for an upcoming feature.

### Patch Version 23.20.5

*Release date: 20-October-2023 *#### Bug fixes **Products table (PIM-1723)** Fixed an issue that prevented clicks on rows in the NextGen products table after using the favourite filter dropdown. ** Products table (PIM-1728)**

Fixed an issue that caused filter settings to not be stored properly in the NextGen products table.

### Patch Version 23.20.4

*Release date: 19-October-2023 *#### Bug fix **Product (PIM-1726)**

Bulk editing did not work in the product table and is now functional again.

### Patch Version 23.20.3

*Release date: 18-October-2023 *#### Improvement **Amazon (ECOM-3800)**

Shipping addresses from Amazon are disregarding the Buyername, as this Buyername is not necessarily tied to a company name or a person. This means the "Ansprechpartner" field in the shipping notes will stay empty.

#### Bug fix **Sales order (FFU-2504)**

An issue affecting the creation of partial deliveries has been resolved.

### Patch Version 23.20.2

*Release date: 18-October-2023*

This version could not be deployed properly due to technical reasons. The bug fix described below is provided in version 23.20.3.

#### Bug fix **Sales order (FFU-2504)**

An issue affecting the creation of partial deliveries has been resolved.

### Release Version 23.20.0

*Release date: 17-October-2023 *#### New features **Invoice (FAC-2462)** Swiss QR Code has been enabled for invoices. ** Amazon Seller App (ECOM-3710)**

A new storage location has been introduced to the Amazon Seller App, showcasing "in transit" bookings from the Amazon FBA Inventory.

#### Improvements **Settings (TAN-3875)** The settings search has been improved to also show results similar to your input query. ** Project API (TAN-3780)** Now available in Beta status. More information can be found here: https://developer.xentral.com/reference/intro. ** Email verification (PF-1858)** In instances using the new login method, users will be logged out after changing their email. On the next login, they will receive a message asking them to verify their email address. This increases the security of the email change process. ** Dispatch center (FFU-2359)** The immediate shop update, triggered when delivery notes are shipped or tracking information is available, will transition to a process starter. This enhancement will speed up processing in the dispatch center and will be gradually introduced to customers. ** Returns API (FFU-2310)** Returns can now be released via API. ** Sales Order API (FFU-2205)**

We aligned the structure and naming conventions across the different sales order API endpoints. You can find further information in the final section of the release notes.

#### Bug fixes **Ticket system (TAN-3822)** An issue affecting certain emails during the ticket import step has been resolved. ** Appstore (PF-1741)** Wrong information about the availability of apps in certain plans was shown in the appstore and has now been removed. ** UPS (FFU-2409)**

When using the printer spooler for macOS, UPS shipping labels were printed with incorrect formatting/ sizing. This issue has been fixed.

Please note: We are still working to resolve issues with printing UPS labels using the printer spooler for Windows.

**Sales order overview (FFU-2245)** The 'mark as released' mass-action on the sales order overview screen is now functional. ** Sales Order API (FFU-2433)** The Sales Order View endpoint was outputting tax rate -1 in positions. This has been fixed. ** Financial accounting export (FAC-2527)** Errors will no longer occur in the Financial Accounting Export for discounts less than 1 euro. ** Financial accounting export (FAC-2520)** Issues with the debitor export functionality when handling a large number of entries have been resolved. ** Receipt of payment (FAC-2466)** Once a credit note is fully refunded in the receipt of payment module, all associated payment transactions are automatically marked as “complete", eliminating manual intervention. This applies to all payment types. ** Financial accounting export (FAC-2450)** Special characters will now display correctly in the Financial Accounting export CSV. ** Invoice (FAC-2432)**

Amazon VCS Invoices will now be correctly marked as paid if the relevant setting (Paid automatically) is selected.

#### Changes to the API **Sales Order API (FFU-2205)**

The structure and naming conventions across the different sales order API endpoints have been aligned.

The following endpoints have been changed or extended:

#### Sales order list

Changes:

- `orderNumber ` renamed to`documentNumber `-` description `renamed to` bodyOutroduction `-` language `is no longer a string, but an object with attribute` iso2` which is the language code
- The `payment ` object is no longer available, `payment ` information is now wrapped under the`financials` key

#### Sales order view

Changes:

- `orderNumber ` renamed to`documentNumber `-` description `renamed to` bodyOutroduction `-` language `is no longer a string, but an object with attribute` iso2` which is the language code
- The `payment ` object is no longer available, `payment ` information is now wrapped under the`financials` key
- `position.tax ` is now one of`{ rate: float, taxText: string} OR { vatCategory: string, taxText: string}`-` delivery `now contains the` shippingMethod `object and the` deliveryTerms` object

Additions:

- added `salesChannel` object
- added `bodyIntroduction `- added` internalDesignation `- added` tags `- added` webId` to positions

## 23.19 Release and Patch Releases

### Patch Version 23.19.7

*Release date: 13-October-2023 *#### Bugfix **Amazon (ECOM-3785)**

A TypeError issue regarding PHP 8.1 compatibility has been fixed.

### Patch Version 23.19.6

*Release date: 12-October-2023 *#### Bugfix **Delivery Dates (FFU-2462)**

An issue regarding PHP 8.1 compatibility has been fixed.

### Patch Version 23.19.4

*Release date: 11-October-2023 *#### Bugfix **Analytics (XIN-641)**

Some analytics endpoints were called in the wrong format. This issue has been fixed.

### Patch Version 23.19.3

*Release date: 10-October-2023 *#### Bugfix **Receipt of payment (FAC-2426)**

Cash book transactions are no longer imported multiple times in Receipt of Payment.

### Release Version 23.19.2

*Release date: 10-October-2023 *#### Improvements **NextGen Settings (TAN-3866)** Add receipts info box is now a nested feature in the letterhead settings. ** Sales Order API (FFU-2142)** Delivery notes can be filtered by the salesOrderId. ** Shipping methods (FFU-1926)** Configuring shipping methods with a preferred Returns shipping method now pulls the default Returns method rather than populating the carrier field in the return label creation with the original DHL shipping method. ** Amazon (ECOM-3632)**

New Amazon shopimporters will always be set to active and demo mode, provided that they have a valid token.

#### Bug fixes **Settings (TAN-3367)** It was possible to reveal the email passwords of any Xentral user of your instance. Now email passwords can't be revealed anymore. ** CSV importer (PIM-1680)** You can now import the "datum_gueltig_bis" field using the CSV Importer. ** Financial accounting export (FAC-2496)** Cancellation invoice PDFs are now properly picked in the DATEV Unternehmen Online exports. ** Financial accounting export (FAC-2493)** In the Financial Accounting Export, the customer/supplier export is now possible even if the settings only contain project-specific consultant numbers. ** DATEV Connect (FAC-2472)**

A 504 error occured when exporting large amounts of invoices. This issue has been fixed.

## 23.18 Release and Patch Releases

### Patch Version 23.18.1

*Release date: 04-October-2023 *#### Bug fix **Dispatch center (FFU-2444)**

Scanning valid barcodes incorrectly triggered warning messages in the dispatch center. This issue has been fixed.

### Release Version 23.18.0

*Release date: 04-October-2023 *#### Improvements **Email (TAN-3824)** Visibility of an email address can be set to "all users". ** Ticket system (TAN-3681)** The Gmail App now supports fetching emails into the ticket system. ** Auth0 (PF-1859)** For Auth0-enabled instances, attempts to change an email address to one already in use by another Xentral user will prompt an error. User needs to be invited instead. ** Sales Order API (FFU-2385)** The Sales Order API now supports non-ASCII characters in email addresses. ** Sendcloud (FFU-2261)**

When autoprinting fails during label creation with Sendcloud, a protocol entry will be added to the delivery note.

#### Bug fixes **Dispatch center (FFU-2419)** Scanning an incorrect barcode in the dispatch center now triggers an immediate warning message to users. ** Sales Order API (FFU-2401)** The Sales Order VIEW Endpoint now returns the ID of the payment method instead of string translations. ** API (FAC-2501)** Fixed an issue where the Cash Register Balance API endpoint incorrectly sourced the cashregisterid, resulting in inaccurate balance calculations. ** Receipt of payment (FAC-2486)** Authenticating FinAPI directly from the Receipt of Payment module now works correctly. ** Financial accounting export (FAC-2484)** Deactivation of CSV validation is now applicable for both Customer and Supplier exports. ** Financial accounting export (FAC-2473)** Checkbox for ignoring already exported documents in the Financial Accounting Export now works correctly for all document types. ** Invoice (FAC-2463)** When a partially cancelled invoice is marked as paid from the Actions menu, the protocol balance will now be correctly set to 0. ** Receipt of payment (FAC-2169)** Ebay payment partial refunds are now imported properly. ** Amazon (ECOM-3721)** For Amazon B2C orders, shipping address name is used instead of buyer name. ** Amazon FBA (ECOM-3708)**

For Amazon FBA orders, differing billing addresses are being respected when generating the invoice.

## 23.17 Release and Patch Releases

### Patch Version 23.17.3

*Release date: 03-October-2023 *#### Improvements **DATEV (FAC-2507)** Removed mandatory validations for DATEV exports, offering more flexibility during the export process. ** API (FAC-2504)**

The posSettings endpoint now includes the VAT ID, enhancing data completeness.

#### Bug fixes **API (FAC-2501)** Fixed an issue where the Cash Register Balance API endpoint incorrectly sourced the cashregisterid, resulting in inaccurate balance calculations. ** Finance Export (FAC-2500)**

Enabled the correction of currency exchange rates in DATEV CSV export, ensuring accurate financial data.

### Patch Version 23.17.2

*Release date: 02-October-2023 *#### Bug Fix **Amazon FBA (ECOM-3760)**

Missing vital information such as street and name in some FBA orders led to failed order imports. This has been fixed.

### Release Version 23.17.0

*Release date: 26-September-2023 *#### Improvements **Sales Order API (FFU-2369)**

Filtering by various external identifiers has been added.

Note: The "externalShopId" parameter will soon be renamed to "externalOrderId".

**Advanced Order Proposal (FFU-2352)** It is now possible to create multiple separate productions for multiple production items in one shot from the advanced order proposal. Previously production items were added as positions in one production, which caused issues in the processing of productions. ** DPD AT (FFU-1776)**

Options for package type and product selections have been added.

#### Bug fixes **NextGen Navbar (TAN-3784)** The arrow icon in front of each page title has been removed, as it redirects the user unintentionally back to the launchpad. ** Printer (FFU-2409)**

When using the printer spooler for macOS, UPS shipping labels were printed with incorrect formatting/ sizing. This issue has been fixed.

Please note: We are still working to resolve issues with printing UPS labels using the printer spooler for Windows.

**Sales order (FFU-1925)** Tables were not summing financial values correctly when values exceeded 1 Mio. This has been fixed. ** Order status indicator (FFU-1822)** The filters from the order status indicator module did not take effect after a sales order was opened. This has been fixed. ** Service order (FFU-1792)** Serial numbers did not disappear from the "in stock" tab after they have been retrieved from stock for delivery notes that were created via a service order. This has been fixed. ** Receipt of payment (FAC-2460)** Import errors are now correctly ignored in subsequent payment imports. ** Financial accounting export (FAC-2450)** Special characters are now correctly displayed in the CSV export. ** Financial accounting export (FAC-2437)** Currency exchange rates in the CSV export are now accurate. ** Contacts (FAC-2328)** The Contacts module will now display the correct balance for customers/suppliers. ** Amazon (FAC-760)** Amazon imports now handle multiple invoices per order correctly. ** Amazon Seller App (ECOM-3579)**

Making a database migration that could potentially run longer for customers that have used the Amazon Seller App asynchronous. This will avoid potential downtimes during the update process.

## 23.16 Release and Patch Releases

### Patch Version 23.16.1

*Release date: 20-September-2023 *#### Bug fix **Shopware 6 (ECOM-3719)**

Fixed a critical bug where order imports from Shopware 6 were failing after the 23.16.0 update, preventing orders and items from being transferred.

### Release Version 23.16.0

*Release date: 19-September-2023 *#### Improvements **HubSpot (TAN-3770)** HubSpot deal sync now maps both, company and contact if a match to both is found via company name and email address. In addition exporting companies and contacts does not overwrite HubSpot's lifecycle stage or deal phase. ** Sales order API (FFU-2350)** Delivery terms default to the customer's terms if omitted or set to empty if specified as null. ** Sales order API (FFU-2348)** If not specified in the payload, tax information for sales order positions now default to information provided by the product. ** Post.AT (FFU-2340)** Users can specify a sender address different from the company address for shipping labels created via Post.AT. This address is utilized in API calls for label creation. ** POS (FAC-2441)** The POS Journal entries list is now accessible, with filters available for Project, Date, and Journal ID. ** Credit note API (FAC-2440)** Users can now create a credit note directly from a return via API. ** POS (FAC-2439)**

Cashier creation/update for POS now has the capability to set an additional authentication PIN and permission level, for use with the upcoming new POS module.

#### Bug fixes **NextGen Settings (TAN-3728)** The chart of accounts was missing some tabs in the NextGen settings. These tabs are now available again. ** Sales order API (FFU-2328)** There was an issue where customers that were created via API without phone number, email or fax could not be used in the sales order import endpoint. This issue has been fixed. ** Project (FFU-2316)** Project warehouse access restriction handling has been fixed in the sales order mini-details. ** Project (FFU-2077)** Fixed an issue where warehouse stock was accessible to unrelated projects despite project-specific warehouse limitations. ** Financial accounting export (FAC-2438)** The Datev export columns "Zusatzinformation - Art 1", "Zusatzinformation- Inhalt 1" and "Zusatzinformation- Art 2" are correctly exported. ** Liabilities (FAC-2433)** Fixed an issue with regular commitments which was causing "0" values to be placed in the database instead of empty fields. ** Receipt of payment (FAC-2426)** Cash book transactions are no longer imported multiple times in Receipt of payment. ** Financial accounting export (FAC-2423)** XML Consolidated amount will now sum up properly in case of sub-cent differences in the new DATEV export. ** FinApi (FAC-2419)** The FinApi import now automatically imports newly created bank accounts in case of a relogin. ** Credit note (FAC-2278)** Credit notes linked to invoices are now marked as done when the residual invoice amount is paid. ** Receipt of payment (FAC-1861)** Fixed an issue where some Amazon V2 Report Fees were not properly assigned to the specified accounts. ** Invoice (FAC-1679)** Early payment discount (skonto) will no longer be displayed as an open amount in the invoice balance. ** Shopify (ECOM-3651)**

When a deviating delivery address with a company name was used, the delivery address could not be imported to Xentral. This issue has been fixed.

## 23.15 Release and Patch Releases

### Patch Version 23.15.2

*Release date: 18-September-2023 *#### Bug fix **Product (PIM-1672)**

The introduction of UUIDs for products incorrectly deactivated the function to copy products in classic design. This issue has been fixed.

### Patch Version 23.15.1

*Release date: 12-September-2023 *#### Improvements **UPS (FFU-1961)**

New shipping method introduced, supporting UPS OAuth authentication.

### Release Version 23.15.0

*Release date: 12-September-2023 *#### New features **Email (TAN-3680)** A new beta feature enables the use of the Gmail API over SMTP for sending emails from Google mail accounts. ** Auth0 (PF-1823)**

Users can now login with the same credentials on multiple Auth0 enabled instances, whenever they are added to separate instances with the same email.

#### Improvements **NextGen NavBar (TAN-3750)** The navigation configurator now automatically updates with new modules. ** NextGen NavBar (TAN-3749)** The new navbar is now hover-activated, offering consistent, easy-to-understand functionality. ** Financial Accounting Export (FAC-2418)** The limitation of 1001 entries per DATEV CSV customer/supplier export file has been removed. ** DATEV (FAC-2410)** An option to exclude previously exported documents is now available in DATEV Connect Online. ** POS API (FAC-2372)** API endpoints for Point Of Sales have been reordered alphabetically. ** Amazon (ECOM-3572)** Improvements have been made to Amazon-related account health status messages. ** Sales Order API (FFU-2220)**

Delivery and Billing addresses have been made optional. If not provided, data will default to entries from the customer master data.

#### Bug fixes **Printer (PF-1831)** Resolved an issue where saving settings overwrote the device API key, affecting the printer spooler. ** Picking Run (FFU-2344)** Fixed an issue where bill of material items were not displayed correctly in the picking run. ** Delivery Notes (FFU-2254)** Additional checks during the processing of delivery notes now enforce all project warehouse restrictions. ** PayPal (FAC-2431)** Automatic credit note matching now accurately considers the original transaction ID for PayPal accounts. ** Amazon (FAC-2413)** During an Amazon VCS import, while creating an invoice, all tax rates from the order will be copied into the new document. ** Receipt of payment (FAC-2409)** Importing transactions in a business account of type CSV now only searches with strings of length larger than three to match credit notes. ** Financial Accounting Export (FAC-2387)** The cost center is now correctly included in the accounts exports in the Financial Accounting export ** Amazon (FAC-2357)**

During amazon VCS imports, delivery threshold based revenue accounts are added to invoices.

## 23.14 Release and Patch Releases

### Patch Version 23.14.4

*Release date: 04-September-2023 *#### Bug fix **Picking list (FFU-2344)**

Not all components of Just-in-time bill of materials were displayed on picking lists. This issue has been fixed.

### Patch Version 23.14.3

*Release date: 31-August-2023 *#### Bug fix **Groups (FFU-2326)**

Discounts that were defined in price groups were displayed in the sales orders, but not actually applied to the item positions. Discounts from price groups are now correctly taken into account.

### Patch Version 23.14.2

*Release date: 31-August-2023 *#### Bug fix **Printer (PF-1831)**

The API key of the printer was overwritten when changes were made in the basic settings, which disconnected the printer from Xentral. This issue has been fixed.

### Release Version 23.14.1

*Release date: 29-August-2023 *#### New features **Bulk editor (PIM-1390)** A "Clear Cell" feature has been added to the bulk editor for convenient removal of cell content. ** Service account (PF-1437)**

Instances where our new identity provider Auth0 is enabled will get a changed service account functionality. Instead of enabling a unique email access, users are asked to invite the specific Xentral eer they want to help them on their instance. This makes tracking more secure and doesn't require automated disabling of the service account.

#### Improvements **Product (PIM-1626)** Boolean columns can now be displayed in the bulk editor as checkbox fields. ** Shopify Payments (FAC-2272)** When a credit note is created from an invoice paid via Shopify Payments, the Shopify refund can now be triggered automatically directly from the credit note. Only full refunds are possible. ** PayPal (FAC-2271)**

Fees are now imported and automatically matched to specified accounts.

#### Bug fixes **Emails (TAN-3719)** Configuration options for the visibility of connected mail addresses among all Xentral users have been added to the email detail view. ** FTP Backup (SRE-1662)** A new option for forcing active mode has been added. ** Delivery Notes (FFU-2254)** Additional checks have been implemented during the processing of delivery notes to enforce all project warehouse restrictions. ** Financial accounting export (FAC-2389)**

The export process has been updated to function properly when manual account bookings are created without an assigned account.

## 23.13 Release and Patch Releases

### Patch Version 23.13.1

*Release date: 23-August-2023 *#### Bug fix **Shopware 6 (ECOM-3641)**

Resolved an issue with sending stock information to Shopware 6.

### Release Version 23.13.0

*Release date: 22-August-2023 *#### New feature **Bulk editor (PIM-1389)**

Introduced undo and redo functionality to the bulk editor, enabling users to reverse or reapply recent actions for enhanced editing control.

#### Improvements **Products API (PIM-1540)** Users can link similar products or accessory products with a source product using API. ** Products API (PIM-1455)** The product manufacturer structure has been changed to an object in the GET product API endpoint for more consistency. ** Printer (PF-1761)** The printer settings have been simplified by adding the setup of the Device API to the same place as the printer settings and splitting the settings into basic and expert settings. ** Returns API (FFU-2275)** Returns can now be filtered by customer and salesOrder. ** API (FAC-2406)**

Updated list endpoints for invoices, credit notes, liabilities, and payment methods to allow attribute filtering and ordering directly on the page.

#### Bug fixes **Follow-Ups (TAN-3685)** Resolved an issue preventing the successful import of follow-ups. ** DHL and Sendcloud (FFU-1088)** Resolved an issue where the weight factor was not applied for Sendcloud and DHL shipments. ** Mollie (FAC-2258)** The amounts for partial or multiple refunds are now correct. ** Business letter templates (FAC-2126)** The variables "Anschreiben" and "Name" were not working in the template for payment advice. This has been fixed. ** Subscription (FAC-2076)** The subscription group and group total are now working correctly for the subscription invoice. ** Time account (FAC-2027)** Resolved an issue causing an unintended UI switch between Classic and NextGen when booking time. ** Import/Export (PIM-1623)** The import of selling prices wasn't possible using the Import/ Export Center. The import function is now working again. ** Delivery note (FFU-2318)** An additional entry for a best before date (BBD)/ batch was wrongfully created for a product when cancelling a delivery note containing a BBD or batch. This has been fixed. ** Returns (FFU-2321)**

The creation of returns resulted in an error 500. This has been fixed.

## 23.12 Release and Patch Releases

### Patch Version 23.12.1

*Release date: 16-August-2023 *#### Bug fixes **Amazon (ECOM-3622)** There have been slowdowns when editing or saving products that are linked to Amazon. This performance issue has been fixed. ** Amazon Vendor DF (ECOM-3620)**

The Amazon Vendor DF shopimporter wrongfully deactivated itself automatically. This issue has been fixed.

### Release Version 23.12.0

*Release date: 16-August-2023 *#### Improvements **Sales Order API (FFU-2220)** Delivery and Billing addresses are now optional. If the address is not provided, the API will default to data from the customer master data. ** Sales Order API (FFU-2145)** Payment terms are now optional. If the payment term is not provided, the API will default to data from the customer master data. ** PayPal (FAC-2334)** Credit notes are now automatically matched to payments for PayPal. ** Performance (FAC-2218)**

Improved performance for liabilities, travel costs, addresses, order and cashier selection over the task module.

#### Bug fixes **DATEV Connect Online (PF-1795)** The menu item for DATEV Connect Online now links to the correct module. ** Printer (PF-1754)** The printer setup in NextGen now correctly displays all the relevant tabs. ** Sales Order API (FFU-2255)**

Status filtering is now functional for the media type "application/vnd.xentral.minimal.v1+json".

## 23.11 Release and Patch Releases

### Patch Version 23.11.3

*Release date: 11-August-2023 *#### Bug fix **Netstock (FFU-2298)**

Issues with netstock export have been fixed.

### Patch Version 23.11.2

*Release date: 09-August-2023 *#### Bug fixes **Amazon (ECOM-3616)** Sales orders from Amazon which were imported with a broken address can now be reimported from Amazon if the date to fetch is set back to the past. ** Amazon (ECOM-3613)**

New Amazon orders will get imported again (albeit with a delay) and no longer get stuck in the intermediate table.

### Patch Version 23.11.1

*Release date: 09-August-2023 *#### Bug fix **Amazon (ECOM-3612)**

This Hotfix contains a fix to mitigate the overlapping of amazon report processing.

### Release Version 23.11.0

*Release date: 08-August-2023 *#### Improvements **Stechuhr (TAN-3708)** A date column has been added to the legacy Stechuhr API. ** NextGen (PIM-1263)** A self-recovery mechanism in case of issues has been implemented in the data table. ** Return Reasons API (FFU-2227)** Implemented API endpoint to retrieve list of active shipping methods. ** Transfers (FFU-2212)** Implemented proper logout in SFTP transfer module. SFTP connections will close and free resources on the server. ** Returns API (FFU-2203)** Create from Sales Order endpoint has been implemented for Returns. ** Returns API (FFU-2201)** The first iteration of a VIEW endpoint has been implemented. ** Product API (PIM-1538)** The following fields have become available in the Products API: isVariant, variantOf, and mainVariant. ** Sales Order API (FFU-2262)**

Language is now set based on customer preferences or system default during import.

#### Bug fixes **Product (PIM-1515)** The notification message displayed after executing bulk deletion has been translated to German. ** Receipt of payment (FAC-2359)** When a user attempts to connect a bank account from a bank which is not supported by FinApi, an appropriate error message appears. ** DATEV BETA (FAC-2356)** PDF exports now include all graphics. ** DATEV BETA (FAC-2354)** In the BETA version of the DATEV Connect Online export, credit notes and liabilities can now be exported successfully. ** Shopify Payments (FAC-2308)**

New option added to assign either import or transaction date to payments.

## 23.10 Release and Patch Releases

### Patch Version 23.10.4

*Release date: 08-August-2023 *#### Bug fix **Amazon (ECOM-3590)**

Fixed an issue with handling Amazon account status to display it in System Health.

### Patch Version 23.10.2

*Release date: 04-August-2023 *#### Bug fix **Amazon (ECOM-3576, ECOM-3482)**

The order import for Amazon will no longer set the delivery address as the billing address.

### Patch Version 23.10.1

*Release date: 02-August-2023 *#### Bug fix **API (PIM-1584)**

An issue that occurred while parsing data has been fixed.

### Release Version 23.10.0

*Release date: 01-August-2023 *#### Improvements **Settings (TAN-3675)** The configuration views for print labels and protocols have been relocated to the expert mode. ** Gmail App (TAN-3674)** The design of the sign-in button has been updated. ** Navigation bar (TAN-3664)** The Navigation bar now remains at full width in the demo version. ** Ticket module (TAN-3574)** The new Ticket Importer now supports decoding of Cp1252 files. ** NextGen user interface (TAN-3533)** The new sidebar is configurable in settings. ** Products API (PIM-1556)** The region of origin has been added to the customs information. ** Returns API (FFU-2264)** A LIST endpoint has been added to the Returns API. ** Sales Order API (FFU-2263)** The shop field is now renamed to salesChannel. ** Minimum stock quantities (FFU-2243)** The availability of the "lagermindestmengen" module has been corrected (available & maintained). ** Delivery Terms API (FFU-2229)** A new list endpoint has been implemented. ** Return Reasons API (FFU-2227)** Implemented API endpoint to retrieve list of active shipping methods. ** Returns API (FFU-2201)** The first iteration of a VIEW endpoint has been implemented. ** Sales Order API (FFU-2186)** The DISPATCH endpoint has been introduced in a BETA version. It triggers the underlying logic as if the dispatching was executed through the UI. ** Payment Methods API (FAC-2358)** An endpoint to retrieve all available methods has been introduced in a BETA version. ** Amazon (ECOM-3491)**

Amazon sales channels are disabled when the RefreshToken expires. This is shown to the customer with an entry in SystemHealth.

#### Bug fixes **Products (PIM-1514)** Fixed an issue where the loading overlay persisted when editing a product. ** Sales order (FFU-1548)** The "partial delivery possible" filter was not working. This has been fixed. ** DATEV BETA (FAC-2335)** The "Buchungstext" for a liability is now populated with the liability number and supplier. ** Business accounts (FAC-1708)** eBay payment fees are now consistently assigned to the correct account and cost center. ** Amazon (ECOM-3457)** The correct carrier and product information for tracking is now sent to Amazon. ** Shopify (ECOM-3431)**

The transmission of freefield values for variants has been restored.

## 23.9 Release and Patch Releases

### Patch Version 23.9.3

*Release date: 31-July-2023 *#### Bug fixes **Shopify (ECOM-3566)** The speed of the sales order import in the Shopify interface has been improved. ** Analytics Dashboard (XIN-33)**

Issues with the UI of the upcoming Analytics app have been resolved.

### Patch Version 23.9.2

*Release date: 27-July-2023 *#### Bug fix **Database (FFU-2247)**

Resolved issues with the initial state of the database before updating the application.

### Patch version 23.9.1

*Release date: 27-July-2023 *#### Bug fixes **Email verification (PF-1744)** Emails couldn't be verified, when the user didn't have edit rights and the email was already set. This has been fixed. ** Printer (PF-1763)**

Resolved issues with not being able to save new printers in version 23.9.0.

### Release Version 23.9.0

*Release date: 25-July-2023 *#### New feature **Returns Portal (PF-1139)**

TheXentralReturns Portal automates the return process for you and for your customers, by allowing them to easily file returns based on their sales orders via a web portal. The returns portal offers features such as return conditions, a customizable web portal, and access to multiple shipping providers.

#### Improvements **Shipping method API (FFU-2207)** An endpoint was implemented to retrieve a list of active shipping methods. ** Returns API (FFU-2202)** An ALPHA-version endpoint for creating a return for a salesOrder was implemented. ** Sales order API (FFU-2181)** An ALPHA-version endpoint for DISPATCH of sales orders was implemented. ** Sales order API (FFU-1769)** Sales order positions can be added to a sales order and the prices are calculated based on the provided data. ** Financial accounting export (FAC-2327)** In the refactored DATEV code we added new validation checks for the CSV exports and a checkbox where this feature can be turned off. To make this more visible to the customer, we added a message which explains that this validation feature can be turned off. ** Receipt of payment (FAC-1644)**

Outgoing payments are now automatically matched to credit notes when appropriate.

#### Bug fixes **Production (FFU-2172)** The process starter 'produktion_berechnen' had a bug which prevented it from running successfully, causing the production traffic lights to remain without update. This has been fixed. ** Financial accounting export (FAC-2345)** Forbidden characters, such as the hashtag, are now removed from the consolidated order id in the XML documents for DATEV company online. ** Amazon (ECOM-3457)**

The correct carrier and product information for tracking is now sent to Amazon.

#### Removal **CUPS printer (PF-1729)**

CLI command for printers was removed for cloud instances.

## 23.8 Release and Patch Releases

### Patch Version 23.8.0

*Release date: 18-July-2023 *#### New feature **HubSpot (TAN-3479)**

The user can now select which project their imported contacts / companies should be associated with.

#### Improvements **Emails (TAN-3521)** The connection details section is now exclusively visible for emails that do not utilize the OAuth connector. ** Ticket module (TAN-3447)** The ticket import functionality has been updated for compatibility with PHP 8.1. ** Sales order API (FFU-1769)**

Sales order positions can be added to a sales order via API and the prices are calculated based on the provided data.

#### Bug fixes **NextGen design (TAN-3571)** Fixed how the new sidebar is being displayed in demo instances. ** Emails (TAN-3575)** Some users could not send emails via an O365 mail account. This issue has been fixed. ** Transfers (FFU-1915)** Resolved existing issues related to SFTP and folder interactions. ** Amazon (ECOM-3507)** There was an issue where stock updates and orders were not synced to Amazon anymore. This issue has been fixed. ** Amazon VCS (ECOM-3405)**

The postage and discount values are now correctly imported by Amazon VCS.

## 23.7 Release and Patch Releases

### Patch Version 23.7.2

*Release date: 13-July-2023*

This patch reverts the changes made to the Transfers module (FFU-1915) in version 23.7.0.

### Release Version 23.7.0

*Release date: 12-July-2023 *#### New feature **Shopify (ECOM-3445)**

An additional filter has been introduced to the Shopify Sales Order import, enabling the import of orders with payment status "Authorized".

#### Improvements **Basic Settings (TAN-3510)** Email configuration in basic settings is now deprecated. All configurations take place in the new Email module. You can migrate your account with one click. ** Product API (PIM-1474)** Consistent data types for amounts have been implemented in Purchase price and Sales prices endpoints. ** Product API (PIM-1462)**

Introduced a new /api/products//purchasePrices endpoint that allows setting supplier and price.

#### Bug fixes **Import templates (TAN-3517)** An issue where the column numbers were overwritten in the English version of the Import Templates module has been addressed. ** Product (PIM-1491)** An incorrect preview image was shown in the drop-down product preview in the product data table of the classic design. This has been fixed, so that the latest version of the image file is displayed. ** Product (PIM-1450)** Resolved an issue where all products were displayed despite an active product filter. ** DPD (FFU-1806)** The "versendet_am" (sent on) field in the "versand" (shipping) table was not filled when printing DPD shipping labels from a delivery note. This has been fixed so that the field is now being filled correctly. ** Transfers (FFU-1915)** (changes made by this ticket were reverted with version 23.7.2)

Resolved issues related to SFTP and folder interactions.

**Shopware 6 (ECOM-3381)**

Matrix products (variants) are now imported correctly from Shopware 6.

## 23.6 Release and Patch Releases

### Release Version 23.6.0

*Release date: 05-July-2023 *#### New feature **Analytics Dashboard (XIN-33)**

The new Overview Dashboard will be enabled for Beta customers throughout this week. Once activated, you can find it in the NextGen UI underAnalytics > Overview dashboard.

#### Improvements **Company Data (TAN-3499)** A new field for the EORI number (Economic Operators´ Registration and Identification number) has been added to the company data. ** Reports (TAN-3263)**

The date filter has been updated to support MySQL 8.

#### Bug fixes **Taxdoo (FAC-2290)** A server error that occurred when using a custom start date in the Taxdoo module has been addressed. ** Business accounts (FAC-2274)** In some cases entries were not imported correctly as they were suspected to be duplicates. In business accounts of type CSV, users can now manually import entries that are suspected duplicates, which will be marked as import errors for your attention. ** Product (PIM-1272)**

An incorrect preview image was shown in the product data table of the classic design. This has been fixed, so that the latest version of the image file is displayed.

## 23.5 Release and Patch Releases

### Release Version 23.5.0

*Release date: 27-June-2023 *#### Improvements **Ticket system (TAN-3451)** The ticket importer has been updated to a new IMAP implementation. ** Product API (PIM-1459)** The same property values that are available for the PATCH endpoint, are now also available for the GET endpoint. ** WooCommerce (ECOM-1193)**

Transfer of product descriptions from Xentral to WooCommerce has been improved for cases where the user utilizes HTML tags.

#### Bug fixes **Ticket system (TAN-3412)** Embedded images are now correctly displayed in the ticket history. ** Import templates (TAN-3194)** An issue with import templates not functioning when using the English user interface has been resolved. ** Product (PIM-1466)** When copying a product, attached files, features and price details were not transferred to the copy correctly. This has been fixed. ** Project (FFU-2095)** An issue with the quick-selection buttons in the logistics/shipping settings, which allow for quick configuration application for pre-defined picking procedures, has been fixed. ** Dispatch center (FFU-2094)** A sound notification is now played again when an incorrect product is scanned. ** DATEV (FAC-2263)**

The sales order number is now included when there is no available invoice. This also applies to refunds. If an incoming payment does not match any document, the transaction code is displayed.

## 23.4 Release and Patch Releases

### Release Version 23.4.0

*Release date: 21-June-2023 *#### Improvements **Financial accounting export (FAC-2216)** Export history has been enabled for all export methods and users can now exclude already sent entries. ** Sales order API (FAC-2223)** Full invoice creation directly from a sales order is now supported. ** Invoice API (FAC-2239)** The * View Invoice*endpoint now includes the customer's email address in the billingAddress object. **Standard API (FFU-1916)** The sales tax for sales order items will be set via the API if provided; otherwise, the product's standard value will be used. ** Amazon Seller App (PIM-1404)** Redundant radio buttons have been removed on the Amazon Seller App product mapping page. ** Product overview table in NextGen (PIM-1324)** Users are now able to delete multiple products on the NextGen product overview table. ** Product API (PIM-1321)** An error message now appears when an endpoint expects a collection of objects but receives a single object. ** Product API (PIM-1240)**

The product category has been added to update and create endpoints.

#### Bug fixes **Delivery note (FFU-2083)** Some delivery notes were mapped to the wrong ID. This issue has been fixed. ** Shopware 5 (ECOM-3322)** The issue preventing the import of more than one order at a time has been resolved. ** Shopify (ECOM-1548)** Business customers/ companies were wrongly imported from Shopify as a contact of type * Other*instead of type * Company*. This issue has been fixed.

## 23.3 Release and Patch Releases

### Patch Version 23.3.2

*Release date: 14-June-2023*

#### Bug fix

Sales orders (FFU-2064)

The delivery handover table in the sales order module did not load correctly. This issue has been fixed.

### Release Version 23.3.1

*Release date: 13-June-2023 *#### Improvements **Products API (PIM-1417)** A * new remaining quantity*field has been added to the * View product*endpoint of the products API. This field is used to synchronize stock information between Xentral and different shops and marketplaces. **Products API (PIM-1407)**

The free field name key was removed from PATCH/POST of the products endpoint.

#### Bug fixes **Xentral Boss app (TAN-1929)** The revenue chart in the Xentral Boss app displayed incorrect data in the month and week tabs. This issue has been fixed. ** Sales Prices API (PIM-1411)** When patching sales prices using the SalesPrice API some unrelated fields were updated. The API now only updates values that were explicitly set in the request. ** Email verification (PF-1551)** Some customers were affected by an issue with the email verification, when confirming the email through a different device/browser than that of their instance. This issue should now be resolved. ** Sales order (FFU-1942)** Some sales orders were incorrectly displayed twice in the sales order overview, when the same shipping method type was used by multiple shipping methods. ** Dropshipping warehouse (FFU-1464)** In some cases, dropshipping orders were not split into the correct number of partial orders, but extra empty orders were created. This has been fixed. ** Mollie (FAC-2194)** The automatic Mollie refund now also works for partial refunds. ** Shopify Payments (FAC-2189)**

When importing Shopify payments, the date shown is now correctly the transaction date instead of the import date.

## 23.2 Release and Patch Releases

### Patch Version 23.2.3

*Release date: 12-June-2023 *#### Bug fix **Amazon (ECOM-3369)**

There have been issues with the creation of invoices when using Amazon VCS where an additional item with ID = 1 has been added. This has been fixed.

### Patch Version 23.2.2

*Release date: 08-June-2023 *#### Bug fix **Amazon (ECOM-3357)**

Some sales orders could not be imported. This has been fixed.

### Release Version 23.2.1

*Release date: 06-June-2023 *#### Improvements **Emails (TAN-3379)** The old email module is now deprecated and a banner has been added to the module for notice. Transitioning to the NextGen Email Module is recommended. ** HubSpot (TAN-2992)** HubSpot data, including contacts and companies, can now be imported based on the lifecycle status. ** Translations (FFU-1901)** All Fulfillment module titles have been translated to the available languages. ** DATEV (FAC-2196)** The export history for DATEV has been improved. ** Kaufland (ECOM-1883)**

A new method to manage new products (EANs) has been added, based on the regulations of Kaufland.

#### Bug fixes **Ticket system (TAN-3375)** There was an issue with the ticket forwarding feature where the entire ticket history was being forwarded to the designated mail address. ** Product overview table in NextGen (PIM-1273)** The preview image in the dropdown product preview, as well as on the product edit page, now correctly reflects the latest version of the file, with the sort field being taken into account. ** Mobile warehouse management (FFU-1875)** Under certain circumstances, multiple positions of the same item were not correctly recorded from intermediate storage when using the Mobile warehouse management app. ** Order proposal (FFU-1810)** Filter settings will be retained and the results displayed after reloading the order proposal page. ** Payment transactions (FAC-2133)** Deleting a collective payment advice no longer incorrectly removes credit note relations in other unrelated payment advice documents. ** Receipt of payment (FAC-1678)** Certain unnecessary Paypal transactions are no longer imported to avoid duplicates. ** Article Module (PIM-1374)** The issue of displaying incorrect thumbnails in the product table's preview has been fixed. ** Online Shops (ECOM-3356)**

In certain cases, sales orders were not completely synced across various shop connections. This has been fixed.

## 23.1 Release and Patch Releases

### Patch Version 23.1.1

*Release date: 05-June-2023 *#### Bug fix **Shopify (ECOM-3347)**

Some sales orders could not be imported. This has been fixed.

### Release Version 23.1.0

*Release date: 30-May-2023 *#### Bug fix **Sales Order (FFU-1647)**

Certain foreign letters were displayed as questions mark and not as correct letters. This has been fixed.