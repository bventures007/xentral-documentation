> **Anmerkung**
>
> Updates von einer XentralVersion 21.x oder älter auf die aktuellste XentralVersion können eine längere Zeit in Anspruch nehmen - abhängig von der Menge an Daten in deiner XentralInstanz. Bitte habe etwas Geduld.

## 23.26 Release and Patch Releases

### Patch Version 23.26.12

*Release date: 11-January-2024 *#### Bug fix **Product (PIM-1889)**

The "Country of origin" field in the product master data was missing an empty option, which caused customers who didn't select an option to have an incorrect entry in their master data. This issue has been fixed.

### Patch Version 23.26.11

*Release date: 09-January-2024 *#### Bug fix **Mobile Inventory App (FFU-2826)**

Resolved several small issues with the Mobile Inventory App.

### Release Version 23.26.10

*Release date: 09-January-2024 *#### New feature **Mobile Inventory App (FFU-2469)**

A new inventory app, which allows you to count your stock using multiple mobile devices at the same time, is now available.

#### Improvements **User (PF-2023)** Users can now be invited more easily, by only adding a name and email, while the related "Contact" can be automatically created and connected in the background. ** Update Button (TAN-4109)** Admins of non-beta instances will find an update button in the navbar whenever a new version is available. ** Settings (TAN-4032)** Project views within settings have been enhanced for a better user experience. ** Settings (TAN-4026)** The "Advanced settings" toggle has been removed. All settings are now enabled or disabled based on license information. ** Navbar (TAN-3973)** New Sales Channels can be accessed. ** Products (PIM-1460)** In the Products module, free fields can now be filtered using the search field. ** Warehouse API (FFU-2636)** If there is no project linked to a warehouse, the endpoint now returns project: NULL instead of a project object with ID = 0. ** Shipping method: Address label (FFU-2633)** The shipping method "Address label" is now available in all licenses again. ** UPS OAuth (FFU-2629)**

UPS will now receive phone + email address provided the GDPR settings are set to allow transferring customer details to shipping carriers.

NOTE: This fix is ONLY applied to the new UPS (OAuth) shipping method. We recommend all users to migrate to the new UPS (OAuth) shipping method.

**Process starter (FFU-2602)** The process starter configuration now displays immediate warnings in case the execution frequency is shorter than allowed. ** DATEV Connect Online (FAC-2576)** Improved the performance of the DATEV Connect Online export. ** Warehouse API (FFU-2530)** An endpoint has been implemented to retrieve items located in a storage location. ** Invoice API (FAC-2753)** The List Invoices API endpoint now includes the possibility of filtering by the ID of the connected sales order. ** Amazon (ECOM-3876)** FBA orders can be configured to be created with a 24h delay. This will improve the handling of differing billing addresses. ** Amazon VCS (ECOM-3853)**

The VCS invoice import will now select the most accurate tax rate for the invoice's country to prevent discrepancies in the calculated tax rate, as long as the "Steuersätze" module is filled with accurate data.

#### Bug fixes **Inventory performance (XIN-781)** The table in the Inventory Performance module now displays the correct data for the 'average retail value' column. ** Inventory performance (XIN-778)** The table in the Inventory Performance module now has the 'Inventory Value' column correctly formatted as a currency, and the missing 'Total Quantity' column is now visible. ** Protocol (PF-1876)** Resolved issue of missing dates in the protocol overview of sales orders following changes in user settings. ** Report (TAN-4123)** Comma and escaping issues in CSV exports in the Report module have been resolved. ** Follow-up (TAN-4079)** Enhanced performance in displaying Stage-view for Follow-ups. ** Layout template attachment (TAN-4054)** Improved error handling in PDF creation. ** Follow-Up (TAN-3041)** Follow-Ups are now correctly displayed in all stages that are set to be shown. ** Item tree (PIM-1870)** Resolved an issue where the item tree displayed deleted categories. All entries in the item tree are now displayed correctly. ** NextGen product table (PIM-1788)** Retaining search field entries when returning from product details to NextGen product table view. ** Product (PIM-1588)** Resolved an issue with the processing of text fields in shops when using bulk processing. ** Sales order (FFU-2804)** Resolved an issue that occured when importing sales orders via API. ** Transfers (FFU-2731)** Resolved an issue where the process starter "api_uebertragen" stopped working when trying to create a PDF with an invalid template. ** Transfers (FFU-2737)** SFTP private key authentication with passphrase is working again. ** Process starter (FFU-2723)** The folgebestaetigung process starter now correctly sends emails only for sales orders with an activated project setting. ** Post.AT (FFU-2709)** The printer from the user settings will now be used if the printer field in the Post.AT shipping method is left empty. ** Netstock (FFU-2703)** Resolved issues with saving SQL statements in the Netstock module. ** Delivery note (FFU-2698)** Fixed the PDF previews for delivery notes that have no tracking numbers. ** GLS (FFU-2692)** The tracking links for GLS were not working. This has been fixed. ** Sales order (FFU-2613)** In the sales order list view, actions in the mini detail were occasionally applied to the incorrect sales order when multiple sales orders were expanded. This has been fixed. ** Return Reasons API (FFU-2611)** Return Reasons API was requiring a project ID which is an optional parameter. This has been fixed so that the full list of return reasons can be obtained without specifying any project ID. ** DPD (FFU-2554)** Resolved an issue where the {TRACKINGNUMMER} variable did not display all tracking numbers for delivery notes with multiple entries. ** Dropshipping Warehouse (FFU-2496)** New options have been added to the Dropshipping Warehouse that improve the logic for how sales orders are processed. ** Dropshipping supplier (FFU-2022)** Corrected an issue where fixed-value discounts were duplicated in split orders. Now, only percentage discounts are copied, while fixed-value discounts stay on the main order. ** Dispatch center (FFU-1940)** The serial number wizard in the dispatch center is now working again. ** Delivery note (FFU-1898)** The quick preview and protocol of delivery notes created for suppliers were displayed incorrectly. This has been fixed. ** Taxdoo (FAC-2742)** Saving Taxdoo configurations with single quotes no longer results in added backslashes. ** Liabilities (FAC-2741)** Adjusted liability tax configurations to prevent the addition of slashes when using single quotes. ** DATEV (FAC-2737)** Amounts in grouped positions of invoices and credit notes get calculated correctly, when the first position is a discount. ** Financial accounting export (FAC-2710)** Resolved an error occurring with 0.00 amount credit notes during export. ** DATEV Company Online (FAC-2706)** In DATEV Company Online, the costCategoryId field will now correctly show the assigned cost center. ** Financial accounting export (FAC-2705)** Tax rate is now properly exported in the Financial Accounting Export for liabilities. ** Cost center (FAC-2682)** Cost centers with more than 10 characters can now be used in the Invoice and respective Accounting exports. ** POS (FAC-2669)** For the new POS, the GET Journal List endpoint will now be properly filterable by salesOrderId and externalOrderNumber. ** DATEV Connect Online (FAC-2625)** Documents, which are exported via Datev XML file export, are no longer excluded in Datev Connect Online. ** Kaufland (ECOM-3974)** Order imports can now accurately identify external products in Xentral using their EANs. ** Amazon VCS (ECOM-3972)** Resolved an issue where promotional discounts were not correctly included in invoices and credit notes from Amazon VCS. ** Amazon (ECOM-3952)** Fixed an issue where "Artikel anhängen" created numerous incorrect entries in the "amazon_merchantgroup" table. ** Amazon Seller App (ECOM-3885)** In-transit stock quantity is set to 0 upon reaching its destination. ** Amazon (ECOM-3867)**

The Amazon shopimporter is now accessible even when all marketplace IDs are disabled.

#### Removal **Amazon MFN (ECOM-3956)**

Support for Amazon's MFN via our Transfer Module, previously facilitated by the Amazon MWS API, has been discontinued.

## 23.24 Release and Patch Releases

### Patch Version 23.24.8

*Release date: 22-December-2023 *#### Bug fix **GLS (FFU-2692)**

The tracking links for GLS were not working. This has been fixed.

### Release Version 23.24.6

*Release date: 05-December-2023 *#### New feature **Inventory Performance**

This new analytics feature allows you to analyze your inventory performance based on product, project or warehouse in Xentral NextGen.

#### Improvements **Contacts (TAN-3713)** When a user creates a new contact with the role employee, that new employee gets access to the same projects as the user creating the contact. ** Service account (PF-2009)** Removed the green notification dot from the service account menu item to reduce confusion among users. ** Xentral UI (PF-2005)** Updated display to show the correct plan for users' instances and a badge indicating participation in the beta program. ** DHL (FFU-2608)** Added a check box to the DHL shipping method that allows you to exclude the components of a JIT (Just in time) bill of materials on the CN22 customs form. ** Transfers (FFU-2572)** Empty SFTP ports will now fall back on the default port 22. ** DHL Express (FFU-2568)** An exception was caused whenever the country settings were empty. This issue has been fixed. ** Post AT (FFU-2564)** Resolved an HTTP 500 error when scanning a parcel from Post AT. ** Delivery notes API (FFU-2527)** Launched the Delivery notes VIEW endpoint. ** Warehouse API (FFU-2455)** Implemented an endpoint for retrieving a list of all storage locations in a warehouse. ** Sales order API (FFU-2361)** Enhanced functionality to allow the import of dedicated discounts for sales orders. ** Process starter (FFU-115)** The process starter configuration now displays a warning for periodic process starters with periods set below the allowed minimum. ** Swiss QR Invoice (FAC-2621)** The Swiss QR Invoice Module is now findable in the appstore and the search bar. ** Financial accounting export (FAC-2614)** Any errors that occur during the CSV export are now collected into a separate log file that is exported together with the CSV output. ** DATEV (FAC-2607)** When a PDF is not found in the archive for DATEV Unternehmen Online and DATEV Connect Online, it will be generated automatically. ** Receipt of payment (FAC-2603)** The transactions in PayPal are checked for doublets independently from the misleading customer/business name. ** DATEV Connect Online (FAC-2600)** The export history is now shown for DATEV Connect Online. ** DATEV Connect Online (FAC-2581)** In any DATEV XML export, the articles are now also grouped by cost centers. ** Financial accounting export (FAC-2495)** Date ranges for previously exported documents are now displayed in the Financial Accounting Export. ** Amazon (ECOM-3814)**

Amazon order import will fetch the VAT ID if a buyer has one.

#### Bug fixes **NextGen Navbar (PIM-1789)** Modules Employees, Calendar, and Production Center now show up in the side navigation when selected in the user preferences. ** Product (PIM-1774)** Resolved a PHP 8.1 error that occurred when importing a bill of materials for a product. ** Transfers (FFU-2582)** Files could not be downloaded from SFTP servers due to issues with file paths. This issue has been fixed. ** Batches (FFU-2378)** Resolved an issue where canceling delivery notes resulted in double batches. ** Batches (FFU-2140)** Batches (pick list profiles) processing sometimes left sales orders unprocessed. This has been fixed. ** Returns (FFU-1997)** The debitor value is now correctly filled on the credit note when created from a return document. ** PayPal (FAC-2731)** Import of PayPal fees now requires a default cost center or revenue account to be set. ** POS (FAC-2727)** When creating a credit note via API from a return, and it's marked as approved, the document number is now correctly populated. ** Shipping tax split (FAC-2638)** The shipping tax split logic is no longer applied when an order is split into partial orders or it is itself a partial order. ** DATEV Connect online (FAC-2625)** Documents, which are exported via Datev XML file export, are no longer excluded in Datev Connect Online. ** Receipt of payment (FAC-2619)** Resolved an issue where Shopify payment transactions were imported twice, but with different names. All Shopify payments are now correctly imported only once. ** Paypal (FAC-2536)** Fees associated with PayPal refunds are now accurately imported as debits during the import process. ** Shipping tax split (FAC-2188)** Ensured accurate import of shipping costs in sales orders and invoices when the shopping cart contains only free products. ** Billbee (ECOM-3929)** An issue with handling incorrect responses from Billbee has been fixed. ** eBay (ECOM-3905)** Due to issues with the ebay_bulkjobs process starter, the stock sync with eBay was not working. This issue has been fixed. ** eBay (ECOM-3903)**

Resolved an issue with the eBay user shop token.

## 23.22 Release and Patch Releases

### Patch Version 23.22.9

*Release date: 15-November-2023 *#### Bug fix **Batches (FFU-2426)**

Resolved an issue with the calculation of batches and best before dates for some specific customers.

### Patch Version 23.22.8

*Release date: 14-November-2023 *#### Bug fix **eBay (ECOM-3858)**

Improved error handling of eBay bulk jobs. Failed jobs should not block the queue anymore.

### Patch Version 23.22.7

*Release date: 13-November-2023 *#### Bug fix **Transfers (FFU-2572)**

Empty SFTP ports will now fall back on the default port 22.

### Patch Version 23.22.6

*Release date: 10-November-2023 *#### Bug fixes **eBay (ECOM-3905)** Due to issues with the ebay_bulkjobs process starter, the stock sync with eBay was not working. This issue has been fixed. ** DHL Express (FFU-2568)**

An exception was caused whenever the country settings were empty. This issue has been fixed.

### Patch Version 23.22.4

*Release date: 09-November-2023 *#### Bug fix **Transfers (FFU-2582)**

Files could not be downloaded from SFTP servers due to issues with file paths. This issue has been fixed.

### Release Version 23.22.3

*Release date: 07-November-2023 *#### Improvements **NextGen Navbar (TAN-3909)** The navigation has been improved to reduce mouse travel time. ** NextGen System Messages (PIM-1752)** A badge indicating system message count has been added to the user avatar in the navigation sidebar. ** User Settings (PF-1969)** Updating your email address will now log you out to ensure you can login with the new email. This change will also update the login email in other instances using the same address. ** Return Reasons API (FFU-2548)** Switched return reason IDs from UUID to auto-increment. ** Deliveries API (FFU-2464)** Added tracking link and carrier name to the payload of the LIST endpoint. Note: Currently not functional for Sendcloud. ** Deliveries API (FFU-2425)** Tracking information has been added to the delivery note LIST endpoint. ** Sales Order API (FFU-2424)** Sales Order Import API now allows importing of shipping costs via a separate parameter object. ** Sales Order API (FFU-2384)** Added effectiveVat to the tax object in positions of the sales order VIEW endpoint. ** Transfers (FFU-2377)** SFTP has been fixed so that modern encryptions are now supported. ** POS API (FAC-2577)**

The GET Journal List endpoint now also contains and can be filtered by the externalOrderNumber field.

#### Bug fixes **Overview Dashboard (XIN-697)** Product SKUs were not showing on the Overview Dashboard, but are now visible again. ** Protocol (PF-1876)** Resolved issue of missing dates in the protocol overview of sales orders following changes in user settings. ** DPD (FFU-2542)** DPD shipping labels with a shipping date on weekends or bank holidays could not be created anymore. There is now a new setting in the DPD shipping method that allows you to automatically set the shipping date to the next business day. ** DPD (FFU-2381)** Tracking numbers were not stored in the invoice when 'complete immediately' is activated in DPD shipping method. This has been fixed. ** Transfers (FFU-1915)** Resolved existing issues related to SFTP and folder interactions. ** Mollie (FAC-2606)** Fixed an error that occurred when the state request parameter was missing. ** DATEV Unternehmen (FAC-2599)** In DATEV Unternehmen exports, zero-amount invoices are now properly ignored regardless of the setting to include them in the CSV export. ** Financial accounting export (FAC-2594)** In Column N, product details will now be displayed when grouped by product. ** Financial accounting export (FAC-2589)** Resolved an issue where the export would fail with a value of 0.00. ** Financial accounting export (FAC-2588)** The account period saved in the settings is now displayed correctly in the financial export CSV files. ** Financial accounting export (FAC-2546)** When exporting accounts, accounts will now be sorted by account id and transaction date. ** Financial accounting export (FAC-2538)** XML consolidatedAmount will now properly match with the sum of the positions. ** Financial accounting export (FAC-2537)** Negative liabilities are now displayed correctly in the DATEV XML exports. ** Amazon (ECOM-3863)** An issue with the transmission of tracking information and shipment numbers from Xentral to Amazon has been fixed. ** Process starter (ECOM-3823)** Resolved an issue where successful cronjob runs were not displayed if below a certain threshold. ** Shopware 6 (ECOM-3375)**

Products with a price of 0 are now correctly imported and displayed as expected.

## 23.21 Release and Patch Releases

### Patch Version 23.21.5

*Release date: 01-November-2023 *#### Bug fix **Amazon (ECOM-3863)**

An issue with the transmission of tracking information and shipment numbers from Xentral to Amazon has been fixed.

### Release Version 23.21.3

*Release date: 31-October-2023 *#### New feature **Revenue Analyzer**

Exclusive to NextGen design, the Revenue Analyzer allows you to analyse your sales order and invoice based revenue by drilling down to the product, sales channel or project level. Try it now and give us your feedback at analytics[at]xentral.com!

#### Improvements **Overview Dashboard (XIN-677)** It is now also possible to calculate your KPIs based on invoices. You can switch between sales order and invoice based KPIs at any time by selecting a new baseline in the page filters. ** Products API (PIM-1567)** Added the "thumbnailId" property. ** Deliveries API (FFU-2425)** Tracking information has been added to the list endpoint. ** Warehouse API (FFU-2382)**

Introduced an endpoint to retrieve all available warehouses in an instance.

#### Bug fix **Export template (TAN-3943)** The CSV export in the Export templates module now correctly interprets special characters. ** Dispatch center (FFU-2483)** The validation for allowed product numbers when scanning items in the dispatch center was not working correctly, resulting in a page load & delayed warning when scanning an incorrect item. This has been fixed. ** Receipt of Payment (FAC-2560)** An issue where selecting the "Complete Bookings" button in Incoming Payments module was producing a 500 error has been fixed. ** Financial accounting export (FAC-2505)** The ContraAccount property type has been changed from "integer" to "string" to prevent conversion to "0". ** Invoice (FAC-2499)** Corrected the cash discount calculation in the protocol. ** Revenue Analyzer (XIN-678)**

An issue with the columns in the Revenue Analyzer table has been fixed.

## 23.20 Release and Patch Releases

### Release Version 23.20.7

*Release date: 24-October-2023 *#### New features **Invoice (FAC-2462)** Swiss QR Code has been enabled for invoices. ** Amazon Seller App (ECOM-3710)**

A new storage location has been introduced to the Amazon Seller App, showcasing "in transit" bookings from the Amazon FBA Inventory.

#### Improvements **Settings (TAN-3875)** The settings search has been improved to also show results similar to your input query. ** Project API (TAN-3780)** Now available in Beta status. More information can be found here: https://developer.xentral.com/reference/intro. ** Email verification (PF-1858)** In instances using the new login method, users will be logged out after changing their email. On the next login, they will receive a message asking them to verify their email address. This increases the security of the email change process. ** Dispatch center (FFU-2359)** The immediate shop update, triggered when delivery notes are shipped or tracking information is available, will transition to a process starter. This enhancement will speed up processing in the dispatch center and will be gradually introduced to customers. ** Returns API (FFU-2310)** Returns can now be released via API. ** Sales Order API (FFU-2205)** We aligned the structure and naming conventions across the different sales order API endpoints. You can find further information in the final section of the release notes. ** Amazon (ECOM-3800)**

Shipping addresses from Amazon are disregarding the Buyername, as this Buyername is not necessarily tied to a company name or a person. This means the "Ansprechpartner" field in the shipping notes will stay empty.

#### Bug fixes **Ticket system (TAN-3822)** An issue affecting certain emails during the ticket import step has been resolved. ** Products table (PIM-1728)** Fixed an issue that caused filter settings to not be stored properly in the NextGen products table. ** Product (PIM-1726)** Bulk editing did not work in the product table and is now functional again. ** Products table (PIM-1723)** Fixed an issue that prevented clicks on rows in the NextGen products table after using the favourite filter dropdown. ** Appstore (PF-1741)** Wrong information about the availability of apps in certain plans was shown in the appstore and has now been removed. ** Sales order (FFU-2504)** An issue affecting the creation of partial deliveries has been resolved. ** UPS (FFU-2409)**

When using the printer spooler for macOS, UPS shipping labels were printed with incorrect formatting/ sizing. This issue has been fixed.

Please note: We are still working to resolve issues with printing UPS labels using the printer spooler for Windows.

**Sales order overview (FFU-2245)** The 'mark as released' mass-action on the sales order overview screen is now functional. ** Sales Order API (FFU-2433)** The Sales Order View endpoint was outputting tax rate -1 in positions. This has been fixed. ** Swiss QR invoice (FAC-2569)** Invoices in draft mode no longer throw errors in the PDF preview if the Swiss QR Invoice module is active. ** Financial accounting export (FAC-2527)** Errors will no longer occur in the Financial Accounting Export for discounts less than 1 euro. ** Financial accounting export (FAC-2520)** Issues with the debitor export functionality when handling a large number of entries have been resolved. ** Receipt of payment (FAC-2466)** Once a credit note is fully refunded in the receipt of payment module, all associated payment transactions are automatically marked as “complete", eliminating manual intervention. This applies to all payment types. ** Financial accounting export (FAC-2450)** Special characters will now display correctly in the Financial Accounting export CSV. ** Invoice (FAC-2432)**

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

### Release Version 23.19.7

*Release date: 17-October-2023 *#### Improvements **NextGen Settings (TAN-3866)** Add receipts info box is now a nested feature in the letterhead settings. ** Sales Order API (FFU-2142)** Delivery notes can be filtered by the salesOrderId. ** Shipping methods (FFU-1926)** Configuring shipping methods with a preferred Returns shipping method now pulls the default Returns method rather than populating the carrier field in the return label creation with the original DHL shipping method. ** Amazon (ECOM-3632)**

New Amazon shopimporters will always be set to active and demo mode, provided that they have a valid token.

#### Bug fixes **Settings (TAN-3367)** It was possible to reveal the email passwords of any Xentral user of your instance. Now email passwords can't be revealed anymore. ** CSV importer (PIM-1680)** You can now import the "datum_gueltig_bis" field using the CSV Importer. ** Financial accounting export (FAC-2496)** Cancellation invoice PDFs are now properly picked in the DATEV Unternehmen Online exports. ** Financial accounting export (FAC-2493)** In the Financial Accounting Export, the customer/supplier export is now possible even if the settings only contain project-specific consultant numbers. ** DATEV Connect (FAC-2472)** A 504 error occured when exporting large amounts of invoices. This issue has been fixed. ** Receipt of payment (FAC-2426)** Cash book transactions are no longer imported multiple times in Receipt of Payment. ** Analytics (XIN-641)** Some analytics endpoints were called in the wrong format. This issue has been fixed. ** Amazon (ECOM-3785)** A TypeError issue regarding PHP 8.1 compatibility has been fixed. ** Delivery Dates (FFU-2462)**

An issue regarding PHP 8.1 compatibility has been fixed.

## 23.18 Release and Patch Releases

### Release Version 23.18.1

*Release date: 10-October-2023 *#### Improvements **Email (TAN-3824)** Visibility of an email address can be set to "all users". ** Ticket system (TAN-3681)** The Gmail App now supports fetching emails into the ticket system. ** Auth0 (PF-1859)** For Auth0-enabled instances, attempts to change an email address to one already in use by another Xentral user will prompt an error. User needs to be invited instead. ** Sales Order API (FFU-2385)** The Sales Order API now supports non-ASCII characters in email addresses. ** Sendcloud (FFU-2261)**

When autoprinting fails during label creation with Sendcloud, a protocol entry will be added to the delivery note.

#### Bug fixes **Dispatch center (FFU-2419)** Scanning an incorrect barcode in the dispatch center now triggers an immediate warning message to users. ** Dispatch center (FFU-2444)** Scanning valid barcodes incorrectly triggered warning messages in the dispatch center. This issue has been fixed. ** Sales Order API (FFU-2401)** The Sales Order VIEW Endpoint now returns the ID of the payment method instead of string translations. ** API (FAC-2501)** Fixed an issue where the Cash Register Balance API endpoint incorrectly sourced the cashregisterid, resulting in inaccurate balance calculations. ** Receipt of payment (FAC-2486)** Authenticating FinAPI directly from the Receipt of Payment module now works correctly. ** Financial accounting export (FAC-2484)** Deactivation of CSV validation is now applicable for both Customer and Supplier exports. ** Financial accounting export (FAC-2473)** Checkbox for ignoring already exported documents in the Financial Accounting Export now works correctly for all document types. ** Invoice (FAC-2463)** When a partially cancelled invoice is marked as paid from the Actions menu, the protocol balance will now be correctly set to 0. ** Receipt of payment (FAC-2169)** Ebay payment partial refunds are now imported properly. ** Amazon (ECOM-3721)** For Amazon B2C orders, shipping address name is used instead of buyer name. ** Amazon FBA (ECOM-3708)**

For Amazon FBA orders, differing billing addresses are being respected when generating the invoice.

## 23.17 Release and Patch Releases

### Release Version 23.17.3

*Release date: 04-October-2023 *#### Improvements **DATEV (FAC-2507)** Removed mandatory validations for DATEV exports, offering more flexibility during the export process. ** API (FAC-2504)** The posSettings endpoint now includes the VAT ID, enhancing data completeness. ** Sales Order API (FFU-2369)**

Filtering by various external identifiers has been added.

Note: The "externalShopId" parameter will soon be renamed to "externalOrderId".

**Advanced Order Proposal (FFU-2352)** It is now possible to create multiple separate productions for multiple production items in one shot from the advanced order proposal. Previously production items were added as positions in one production, which caused issues in the processing of productions. ** DPD AT (FFU-1776)**

Options for package type and product selections have been added.

#### Bug fixes **NextGen Navbar (TAN-3784)** The arrow icon in front of each page title has been removed, as it redirects the user unintentionally back to the launchpad. ** Printer (FFU-2409)**

When using the printer spooler for macOS, UPS shipping labels were printed with incorrect formatting/ sizing. This issue has been fixed.

Please note: We are still working to resolve issues with printing UPS labels using the printer spooler for Windows.

**Sales order (FFU-1925)** Tables were not summing financial values correctly when values exceeded 1 Mio. This has been fixed. ** Order status indicator (FFU-1822)** The filters from the order status indicator module did not take effect after a sales order was opened. This has been fixed. ** Service order (FFU-1792)** Serial numbers did not disappear from the "in stock" tab after they have been retrieved from stock for delivery notes that were created via a service order. This has been fixed. ** Receipt of payment (FAC-2460)** Import errors are now correctly ignored in subsequent payment imports. ** Finance Export (FAC-2500)** Enabled the correction of currency exchange rates in DATEV CSV export, ensuring accurate financial data. ** Financial accounting export (FAC-2450)** Special characters are now correctly displayed in the CSV export. ** Financial accounting export (FAC-2437)** Currency exchange rates in the CSV export are now accurate. ** Contacts (FAC-2328)** The Contacts module will now display the correct balance for customers/suppliers. ** API (FAC-2501)** Fixed an issue where the Cash Register Balance API endpoint incorrectly sourced the cashregisterid, resulting in inaccurate balance calculations. ** Amazon (FAC-760)** Amazon imports now handle multiple invoices per order correctly. ** Amazon Seller App (ECOM-3579)**

Making a database migration that could potentially run longer for customers that have used the Amazon Seller App asynchronous. This will avoid potential downtimes during the update process.

## 23.16 Release and Patch Releases

### Patch Version 23.16.5

*Release date: 02-Octobre-2023 *#### Bug fix **Amazon FBA (ECOM-3760)**

Missing vital information such as street and name in some FBA orders led to failed order imports. This has been fixed.

### Patch Version 23.16.4

*Release date: 27-September-2023*

Versions 23.16.2 and 23.16.3 could not be released for technical reasons.

#### Bug fix **Printer (FFU-2409)**

When using the printer spooler for macOS, UPS shipping labels were printed with incorrect formatting/ sizing. This issue has been fixed.

Please note: We are still working to resolve issues with printing UPS labels using the printer spooler for Windows.

### Release Version 23.16.1

*Release date: 26-September-2023 *#### Improvements **HubSpot (TAN-3770)** HubSpot deal sync now maps both, company and contact if a match to both is found via company name and email address. In addition exporting companies and contacts does not overwrite HubSpot's lifecycle stage or deal phase. ** Sales order API (FFU-2350)** Delivery terms default to the customer's terms if omitted or set to empty if specified as null. ** Sales order API (FFU-2348)** If not specified in the payload, tax information for sales order positions now default to information provided by the product. ** Post.AT (FFU-2340)** Users can specify a sender address different from the company address for shipping labels created via Post.AT. This address is utilized in API calls for label creation. ** POS (FAC-2441)** The POS Journal entries list is now accessible, with filters available for Project, Date, and Journal ID. ** Credit note API (FAC-2440)** Users can now create a credit note directly from a return via API. ** POS (FAC-2439)**

Cashier creation/update for POS now has the capability to set an additional authentication PIN and permission level, for use with the upcoming new POS module.

#### Bug fixes **NextGen Settings (TAN-3728)** The chart of accounts was missing some tabs in the NextGen settings. These tabs are now available again. ** Sales order API (FFU-2328)** There was an issue where customers that were created via API without phone number, email or fax could not be used in the sales order import endpoint. This issue has been fixed. ** Project (FFU-2316)** Project warehouse access restriction handling has been fixed in the sales order mini-details. ** Project (FFU-2077)** Fixed an issue where warehouse stock was accessible to unrelated projects despite project-specific warehouse limitations. ** Financial accounting export (FAC-2438)** The Datev export columns "Zusatzinformation - Art 1", "Zusatzinformation- Inhalt 1" and "Zusatzinformation- Art 2" are correctly exported. ** Liabilities (FAC-2433)** Fixed an issue with regular commitments which was causing "0" values to be placed in the database instead of empty fields. ** Receipt of payment (FAC-2426)** Cash book transactions are no longer imported multiple times in Receipt of payment. ** Financial accounting export (FAC-2423)** XML Consolidated amount will now sum up properly in case of sub-cent differences in the new DATEV export. ** FinApi (FAC-2419)** The FinApi import now automatically imports newly created bank accounts in case of a relogin. ** Credit note (FAC-2278)** Credit notes linked to invoices are now marked as done when the residual invoice amount is paid. ** Receipt of payment (FAC-1861)** Fixed an issue where some Amazon V2 Report Fees were not properly assigned to the specified accounts. ** Invoice (FAC-1679)** Early payment discount (skonto) will no longer be displayed as an open amount in the invoice balance. ** Shopify (ECOM-3651)** When a deviating delivery address with a company name was used, the delivery address could not be imported to Xentral. This issue has been fixed. ** Shopware 6 (ECOM-3719)**

Fixed a critical bug where sales order imports from Shopware 6 were failing, preventing orders and items from being transferred.

## 23.15 Release and Patch Releases

### Patch Version 23.15.6

*Release date: 25-September-2023 *#### Bug fix **Printer (FFU-2409)**

When using the printer spooler for macOS, UPS shipping labels were printed with incorrect formatting/ sizing. This issue has been fixed.

Please note: We are still working to resolve issues with printing UPS labels using the printer spooler for Windows.

### Patch Version 23.15.5

*Release date: 21-September-2023 *#### Bug fix **Amazon Seller App (ECOM-3579)**

Making a database migration that could potentially run longer for customers that have used the Amazon Seller App asynchronous. This will avoid potential downtimes during the update process.

### Patch Version 23.15.4

*Release date: 20-September-2023*

This release is solving a problem with a database migration that took longer than it should have. As a result, some customers might have experienced an unresponsive system for an extended period of time during the version update.

### Patch Version 23.15.3

*Release date: 20-September-2023 *#### Bug fix **Overview tables (CCI-1893)**

The overview tables did not load correctly for admin users when using Google Chrome as a browser. This has been fixed.

### Release Version 23.15.2

*Release date: 19-September-2023 *#### New features **Email (TAN-3680)** A new beta feature enables the use of the Gmail API over SMTP for sending emails from Google mail accounts. ** Auth0 (PF-1823)**

Users can now login with the same credentials on multiple Auth0 enabled instances, whenever they are added to separate instances with the same email.

#### Improvements **NextGen NavBar (TAN-3750)** The navigation configurator now automatically updates with new modules. ** NextGen NavBar (TAN-3749)** The new navbar is now hover-activated, offering consistent, easy-to-understand functionality. ** Financial Accounting Export (FAC-2418)** The limitation of 1001 entries per DATEV CSV customer/supplier export file has been removed. ** DATEV (FAC-2410)** An option to exclude previously exported documents is now available in DATEV Connect Online. ** POS API (FAC-2372)** API endpoints for Point Of Sales have been reordered alphabetically. ** Amazon (ECOM-3572)** Improvements have been made to Amazon-related account health status messages. ** Sales Order API (FFU-2220)** Delivery and Billing addresses have been made optional. If not provided, data will default to entries from the customer master data. ** UPS (FFU-1961)**

New shipping method introduced, supporting UPS OAuth authentication.

#### Bug fixes **Product (PIM-1672)** The introduction of UUIDs for products incorrectly deactivated the function to copy products in classic design. This issue has been fixed. ** Printer (PF-1831)** Resolved an issue where saving settings overwrote the device API key, affecting the printer spooler. ** Picking Run (FFU-2344)** Fixed an issue where bill of material items were not displayed correctly in the picking run. ** Delivery Notes (FFU-2254)** Additional checks during the processing of delivery notes now enforce all project warehouse restrictions. ** PayPal (FAC-2431)** Automatic credit note matching now accurately considers the original transaction ID for PayPal accounts. ** Amazon (FAC-2413)** During an Amazon VCS import, while creating an invoice, all tax rates from the order will be copied into the new document. ** Receipt of payment (FAC-2409)** Importing transactions in a business account of type CSV now only searches with strings of length larger than three to match credit notes. ** Financial Accounting Export (FAC-2387)** The cost center is now correctly included in the accounts exports in the Financial Accounting export ** Amazon (FAC-2357)**

During amazon VCS imports, delivery threshold based revenue accounts are added to invoices.

## 23.14 Release and Patch Releases

### Release Version 23.14.4

*Release date: 19-September-2023 *#### New features **Bulk editor (PIM-1390)** A "Clear Cell" feature has been added to the bulk editor for convenient removal of cell content. ** Service account (PF-1437)**

Instances where our new identity provider Auth0 is enabled will get a changed service account functionality. Instead of enabling a unique email access, users are asked to invite the specific Xentral eer they want to help them on their instance. This makes tracking more secure and doesn't require automated disabling of the service account.

#### Improvements **Product (PIM-1626)** Boolean columns can now be displayed in the bulk editor as checkbox fields. ** Shopify Payments (FAC-2272)** When a credit note is created from an invoice paid via Shopify Payments, the Shopify refund can now be triggered automatically directly from the credit note. Only full refunds are possible. ** PayPal (FAC-2271)**

Fees are now imported and automatically matched to specified accounts.

#### Bug fixes **Emails (TAN-3719)** Configuration options for the visibility of connected mail addresses among all Xentral users have been added to the email detail view. ** FTP Backup (SRE-1662)** A new option for forcing active mode has been added. ** Delivery Notes (FFU-2254)** Additional checks have been implemented during the processing of delivery notes to enforce all project warehouse restrictions. ** Financial accounting export (FAC-2389)** The export process has been updated to function properly when manual account bookings are created without an assigned account. ** Picking list (FFU-2344)** Not all components of Just-in-time bill of materials were displayed on picking lists. This issue has been fixed. ** Groups (FFU-2326)** Discounts that were defined in price groups were displayed in the sales orders, but not actually applied to the item positions. Discounts from price groups are now correctly taken into account. ** Printer (PF-1831)**

The API key of the printer was overwritten when changes were made in the basic settings, which disconnected the printer from Xentral. This issue has been fixed.

## 23.13 Release and Patch Releases

### Patch Version 23.13.4

*Release date: 31-August-2023 *#### Bug fix **Groups (FFU-2326)**

Discounts that were defined in price groups were displayed in the sales orders, but not actually applied to the item positions. Discounts from price groups are now correctly taken into account.

### Patch Version 23.13.2

*Release date: 31-August-2023 *#### Bug fix **Printer (PF-1831)**

The API key of the printer was overwritten when changes were made in the basic settings, which disconnected the printer from Xentral. This issue has been fixed.

### Release Version 23.13.1

*Release date: 29-August-2023 *#### Improvements **Products API (PIM-1540)** Users can link similar products or accessory products with a source product using API. ** Products API (PIM-1455)** The product manufacturer structure has been changed to an object in the GET product API endpoint for more consistency. ** Printer (PF-1761)** The printer settings have been simplified by adding the setup of the Device API to the same place as the printer settings and splitting the settings into basic and expert settings. ** Returns API (FFU-2275)** Returns can now be filtered by customer and salesOrder. ** API (FAC-2406)**

Updated list endpoints for invoices, credit notes, liabilities, and payment methods to allow attribute filtering and ordering directly on the page.

#### Bug fixes **Follow-Ups (TAN-3685)** Resolved an issue preventing the successful import of follow-ups. ** DHL and Sendcloud (FFU-1088)** Resolved an issue where the weight factor was not applied for Sendcloud and DHL shipments. ** Mollie (FAC-2258)** The amounts for partial or multiple refunds are now correct. ** Business letter templates (FAC-2126)** The variables "Anschreiben" and "Name" were not working in the template for payment advice. This has been fixed. ** Subscription (FAC-2076)** The subscription group and group total are now working correctly for the subscription invoice. ** Time account (FAC-2027)** Resolved an issue causing an unintended UI switch between Classic and NextGen when booking time. ** Import/Export (PIM-1623)** The import of selling prices wasn't possible using the Import/ Export Center. The import function is now working again. ** Delivery note (FFU-2318)** An additional entry for a best before date (BBD)/ batch was wrongfully created for a product when cancelling a delivery note containing a BBD or batch. This has been fixed. ** Returns (FFU-2321)**

The creation of returns resulted in an error 500. This has been fixed.

## 23.12 Release and Patch Releases

### Patch Version 23.12.6

*Release date: 23-August-2023 *#### Bug fix **Shopware 6 (ECOM-3641)**

Resolved an issue with sending stock information to Shopware 6.

### Release Version 23.12.5

*Release date: 22-August-2023 *#### Improvements **Sales Order API (FFU-2220)** Delivery and Billing addresses are now optional. If the address is not provided, the API will default to data from the customer master data. ** Sales Order API (FFU-2145)** Payment terms are now optional. If the payment term is not provided, the API will default to data from the customer master data. ** PayPal (FAC-2334)** Credit notes are now automatically matched to payments for PayPal. ** Performance (FAC-2218)**

Improved performance for liabilities, travel costs, addresses, order and cashier selection over the task module.

#### Bug fixes **DATEV Connect Online (PF-1795)** The menu item for DATEV Connect Online now links to the correct module. ** Printer (PF-1754)** The printer setup in NextGen now correctly displays all the relevant tabs. ** Sales Order API (FFU-2255)** Status filtering is now functional for the media type "application/vnd.xentral.minimal.v1+json". ** Import/Export (PIM-1623)** The import of selling prices wasn't possible using the Import/ Export Center. The import function is now working again. ** Delivery note (FFU-2318)** An additional entry for a best before date (BBD)/ batch was wrongfully created for a product when cancelling a delivery note containing a BBD or batch. This has been fixed. ** Returns (FFU-2321)**

The creation of returns resulted in an error 500. This has been fixed.

## 23.11 Release and Patch Releases

### Patch Version 23.11.4

*Release date: 16-August-2023 *#### Bug fixes **Amazon (ECOM-3622)** There have been slowdowns when editing or saving products that are linked to Amazon. This performance issue has been fixed. ** Amazon Vendor DF (ECOM-3620)**

The Amazon Vendor DF shopimporter wrongfully deactivated itself automatically. This issue has been fixed.

### Release Version 23.11.3

*Release date: 16-August-2023 *#### Improvements **Stechuhr (TAN-3708)** A date column has been added to the legacy Stechuhr API. ** NextGen (PIM-1263)** A self-recovery mechanism in case of issues has been implemented in the data table. ** Return Reasons API (FFU-2227)** Implemented API endpoint to retrieve list of active shipping methods. ** Transfers (FFU-2212)** Implemented proper logout in SFTP transfer module. SFTP connections will close and free resources on the server. ** Returns API (FFU-2203)** Create from Sales Order endpoint has been implemented for Returns. ** Returns API (FFU-2201)** The first iteration of a VIEW endpoint has been implemented. ** Product API (PIM-1538)** The following fields have become available in the Products API: isVariant, variantOf, and mainVariant. ** Sales Order API (FFU-2262)**

Language is now set based on customer preferences or system default during import.

#### Bug fixes **Product (PIM-1515)** The notification message displayed after executing bulk deletion has been translated to German. ** Receipt of payment (FAC-2359)** When a user attempts to connect a bank account from a bank which is not supported by FinApi, an appropriate error message appears. ** DATEV BETA (FAC-2356)** PDF exports now include all graphics. ** DATEV BETA (FAC-2354)** In the BETA version of the DATEV Connect Online export, credit notes and liabilities can now be exported successfully. ** Shopify Payments (FAC-2308)**

New option added to assign either import or transaction date to payments.

## 23.10 Release and Patch Releases

### Patch Version 23.10.8

*Release date: 11-August-2023 *#### Bug fix **Netstock (FFU-2298)**

Issues with netstock export have been fixed.

### Patch Version 23.10.7

*Release date: 09-August-2023 *#### Bug fixes **Amazon (ECOM-3616)** Sales orders from Amazon which were imported with a broken address can now be reimported from Amazon if the date to fetch is set back to the past. ** Amazon (ECOM-3613)**

New Amazon orders will get imported again (albeit with a delay) and no longer get stuck in the intermediate table.

### Patch Version 23.10.6

*Release date: 09-August-2023 *#### Bug fix **Amazon (ECOM-3612)**

This Hotfix contains a fix to mitigate the overlapping of amazon report processing.

### Release Version 23.10.5

*Release date: 08-August-2023 *#### Improvements **Settings (TAN-3675)** The configuration views for print labels and protocols have been relocated to the expert mode. ** Gmail App (TAN-3674)** The design of the sign-in button has been updated. ** Navigation bar (TAN-3664)** The Navigation bar now remains at full width in the demo version. ** Ticket module (TAN-3574)** The new Ticket Importer now supports decoding of Cp1252 files. ** NextGen user interface (TAN-3533)** The new sidebar is configurable in settings. ** Products API (PIM-1556)** The region of origin has been added to the customs information. ** Returns API (FFU-2264)** A LIST endpoint has been added to the Returns API. ** Sales Order API (FFU-2263)** The shop field is now renamed to salesChannel. ** Minimum stock quantities (FFU-2243)** The availability of the "lagermindestmengen" module has been corrected (available & maintained). ** Delivery Terms API (FFU-2229)** A new list endpoint has been implemented. ** Return Reasons API (FFU-2227)** Implemented API endpoint to retrieve list of active shipping methods. ** Returns API (FFU-2201)** The first iteration of a VIEW endpoint has been implemented. ** Sales Order API (FFU-2186)** The DISPATCH endpoint has been introduced in a BETA version. It triggers the underlying logic as if the dispatching was executed through the UI. ** Payment Methods API (FAC-2358)** An endpoint to retrieve all available methods has been introduced in a BETA version. ** Amazon (ECOM-3491)**

Amazon sales channels are disabled when the RefreshToken expires. This is shown to the customer with an entry in SystemHealth.

#### Bug fixes **API (PIM-1584)** An issue that occurred while parsing data has been fixed. ** Products (PIM-1514)** Fixed an issue where the loading overlay persisted when editing a product. ** Sales order (FFU-1548)** The "partial delivery possible" filter was not working. This has been fixed. ** DATEV BETA (FAC-2335)** The "Buchungstext" for a liability is now populated with the liability number and supplier. ** Business accounts (FAC-1708)** eBay payment fees are now consistently assigned to the correct account and cost center. ** Amazon (ECOM-3576, ECOM-3482)** The order import for Amazon will no longer set the delivery address as the billing address. ** Amazon (ECOM-3590)** Fixed an issue with handling Amazon account status to display it in System Health. ** Amazon (ECOM-3457)** The correct carrier and product information for tracking is now sent to Amazon. ** Shopify (ECOM-3431)**

The transmission of freefield values for variants has been restored.

## 23.9 Release and Patch Releases

### Release Version 23.9.3

*Release date: 01-August-2023 *#### New features **Returns Portal (PF-1139)** TheXentralReturns Portal automates the return process for you and for your customers, by allowing them to easily file returns based on their sales orders via a web portal. The returns portal offers features such as return conditions, a customizable web portal, and access to multiple shipping providers. ** Analytics Dashboard (XIN-33)**

The Overview Dashboard helps you stay on top of your business operations by tracking important key performance indicators (KPIs). The KPIs in the overview are structured along three critical areas in your value chain: Business insights, Sales insights, and Warehouse insights. The goal is to give you a quick indication about your organization's health and support you in taking data-driven decisions.

#### Improvements **Shipping method API (FFU-2207)** An endpoint was implemented to retrieve a list of active shipping methods. ** Returns API (FFU-2202)** An ALPHA-version endpoint for creating a return for a salesOrder was implemented. ** Sales order API (FFU-2181)** An ALPHA-version endpoint for DISPATCH of sales orders was implemented. ** Sales order API (FFU-1769)** Sales order positions can be added to a sales order and the prices are calculated based on the provided data. ** Financial accounting export (FAC-2327)** In the refactored DATEV code we added new validation checks for the CSV exports and a checkbox where this feature can be turned off. To make this more visible to the customer, we added a message which explains that this validation feature can be turned off. ** Receipt of payment (FAC-1644)**

Outgoing payments are now automatically matched to credit notes when appropriate.

#### Bug fixes **Printer (PF-1763)** Resolved issues with not being able to save new printers in version 23.9.0. ** Email verification (PF-1744)** Emails couldn't be verified, when the user didn't have edit rights and the email was already set. This has been fixed. ** Production (FFU-2172)** The process starter 'produktion_berechnen' had a bug which prevented it from running successfully, causing the production traffic lights to remain without update. This has been fixed. ** Financial accounting export (FAC-2345)** Forbidden characters, such as the hashtag, are now removed from the consolidated order id in the XML documents for DATEV company online. ** Amazon (ECOM-3457)**

The correct carrier and product information for tracking is now sent to Amazon.

#### Removal **CUPS printer (PF-1729)**

CLI command for printers was removed for cloud instances.

## 23.8 Release and Patch Releases

### Patch Version 23.8.5

*Release date: 28-July-2023 *#### Bug fix **Shopify (ECOM-3566)**

The speed of the sales order import in the Shopify interface has been improved.

### Patch version 23.8.4

*Release date: 28-July-2023*

Issues with the UI of the upcoming Analytics app have been resolved.

### Patch version 23.8.3

*Release date: 27-July-2023*

Versions 23.8.1, 23.8.2, and 23.8.3 resolved issues with the initial state of the database before updating the application.

### Release Version 23.8.0

*Release date: 25-July-2023 *#### New feature **HubSpot (TAN-3479)**

The user can now select which project their imported contacts / companies should be associated with.

#### Improvements **Emails (TAN-3521)** The connection details section is now exclusively visible for emails that do not utilize the OAuth connector. ** Ticket module (TAN-3447)** The ticket import functionality has been updated for compatibility with PHP 8.1. ** Sales order API (FFU-1769)**

Sales order positions can be added to a sales order via API and the prices are calculated based on the provided data.

#### Bug fixes **NextGen design (TAN-3571)** Fixed how the new sidebar is being displayed in demo instances. ** Emails (TAN-3575)** Some users could not send emails via an O365 mail account. This issue has been fixed. ** Transfers (FFU-1915)** Resolved existing issues related to SFTP and folder interactions. ** Amazon (ECOM-3507)** There was an issue where stock updates and orders were not synced to Amazon anymore. This issue has been fixed. ** Amazon VCS (ECOM-3405)**

The postage and discount values are now correctly imported by Amazon VCS.

## 23.7 Release and Patch Releases

### Release Version 23.7.2

*Release date: 18-July-2023 *#### New feature **Shopify (ECOM-3445)**

An additional filter has been introduced to the Shopify Sales Order import, enabling the import of orders with payment status "Authorized".

#### Improvements **Basic Settings (TAN-3510)** Email configuration in basic settings is now deprecated. All configurations take place in the new Email module. You can migrate your account with one click. ** Product API (PIM-1474)** Consistent data types for amounts have been implemented in Purchase price and Sales prices endpoints. ** Product API (PIM-1462)**

Introduced a new /api/products//purchasePrices endpoint that allows setting supplier and price.

#### Bug fixes **Import templates (TAN-3517)** An issue where the column numbers were overwritten in the English version of the Import Templates module has been addressed. ** Product (PIM-1491)** An incorrect preview image was shown in the drop-down product preview in the product data table of the classic design. This has been fixed, so that the latest version of the image file is displayed. ** Product (PIM-1450)** Resolved an issue where all products were displayed despite an active product filter. ** DPD (FFU-1806)** The "versendet_am" (sent on) field in the "versand" (shipping) table was not filled when printing DPD shipping labels from a delivery note. This has been fixed so that the field is now being filled correctly. ** Shopware 6 (ECOM-3381)**

Matrix products (variants) are now imported correctly from Shopware 6.

## 23.6 Release and Patch Releases

### Release Version 23.6.0

*Release date: 11-July-2023 *#### Improvements **Company Data (TAN-3499)** A new field for the EORI number (Economic Operators´ Registration and Identification number) has been added to the company data. ** Reports (TAN-3263)**

The date filter has been updated to support MySQL 8.

#### Bug fixes **Taxdoo (FAC-2290)** A server error that occurred when using a custom start date in the Taxdoo module has been addressed. ** Business accounts (FAC-2274)** In some cases entries were not imported correctly as they were suspected to be duplicates. In business accounts of type CSV, users can now manually import entries that are suspected duplicates, which will be marked as import errors for your attention. ** Product (PIM-1272)**

An incorrect preview image was shown in the product data table of the classic design. This has been fixed, so that the latest version of the image file is displayed.

## 23.5 Release and Patch Releases

### Release Version 23.5.3

*Release date: 04-July-2023 *#### Improvements **Ticket system (TAN-3451)** The ticket importer has been updated to a new IMAP implementation. ** Product API (PIM-1459)** The same property values that are available for the PATCH endpoint, are now also available for the GET endpoint. ** WooCommerce (ECOM-1193)**

Transfer of product descriptions from Xentral to WooCommerce has been improved for cases where the user utilizes HTML tags.

#### Bug fixes **Ticket system (TAN-3412)** Embedded images are now correctly displayed in the ticket history. ** Import templates (TAN-3194)** An issue with import templates not functioning when using the English user interface has been resolved. ** Product (PIM-1466)** When copying a product, attached files, features and price details were not transferred to the copy correctly. This has been fixed. ** Project (FFU-2095)** An issue with the quick-selection buttons in the logistics/shipping settings, which allow for quick configuration application for pre-defined picking procedures, has been fixed. ** Dispatch center (FFU-2094)** A sound notification is now played again when an incorrect product is scanned. ** DATEV (FAC-2263)**

The sales order number is now included when there is no available invoice. This also applies to refunds. If an incoming payment does not match any document, the transaction code is displayed.

## 23.4 Release and Patch Releases

### Release Version 23.4.0

*Release date: 27-June-2023 *#### Improvements **Financial accounting export (FAC-2216)** Export history has been enabled for all export methods and users can now exclude already sent entries. ** Sales order API (FAC-2223)** Full invoice creation directly from a sales order is now supported. ** Invoice API (FAC-2239)** The * View Invoice*endpoint now includes the customer's email address in the billingAddress object. **Standard API (FFU-1916)** The sales tax for sales order items will be set via the API if provided; otherwise, the product's standard value will be used. ** Amazon Seller App (PIM-1404)** Redundant radio buttons have been removed on the Amazon Seller App product mapping page. ** Product overview table in NextGen (PIM-1324)** Users are now able to delete multiple products on the NextGen product overview table. ** Product API (PIM-1321)** An error message now appears when an endpoint expects a collection of objects but receives a single object. ** Product API (PIM-1240)**

The product category has been added to update and create endpoints.

#### Bug fixes **Delivery note (FFU-2083)** Some delivery notes were mapped to the wrong ID. This issue has been fixed. ** Shopware 5 (ECOM-3322)** The issue preventing the import of more than one order at a time has been resolved. ** Shopify (ECOM-1548)** Business customers/ companies were wrongly imported from Shopify as a contact of type * Other*instead of type * Company*. This issue has been fixed.

## 23.3 Release and Patch Releases

### Release Version 23.3.3

*Release date: 20-June-2023 *#### Improvements **Products API (PIM-1417)** A new * remaining quantity*field has been added to the * View product*endpoint of the products API. This field is used to synchronize stock information between Xentral and different shops and marketplaces. **Products API (PIM-1407)**

The free field name key was removed from PATCH/POST of the products endpoint.

#### Bug fixes **Xentral Boss app (TAN-1929)** The revenue chart in the Xentral Boss app displayed incorrect data in the month and week tabs. This issue has been fixed. ** Sales Prices API (PIM-1411)** When patching sales prices using the SalesPrice API some unrelated fields were updated. The API now only updates values that were explicitly set in the request. ** Email verification (PF-1551)**

Some customers were affected by an issue with the email verification, when confirming the email through a different device/browser than that of their instance. This issue should now be resolved.

Sales order (FFU-2064)

The delivery handover table in the sales order module did not load correctly. This issue has been fixed.

**Sales order (FFU-1942)** Some sales orders were incorrectly displayed twice in the sales order overview, when the same shipping method type was used by multiple shipping methods. ** Dropshipping warehouse (FFU-1464)** In some cases, dropshipping orders were not split into the correct number of partial orders, but extra empty orders were created. This has been fixed. ** Mollie (FAC-2194)** The automatic Mollie refund now also works for partial refunds. ** Shopify Payments (FAC-2189)**

When importing Shopify payments, the date shown is now correctly the transaction date instead of the import date.

## 23.2 Release and Patch Releases

### Release Version 23.2.3

*Release date: 13-June-2023 *#### Improvements **Emails (TAN-3379)** The old email module is now deprecated and a banner has been added to the module for notice. Transitioning to the NextGen Email Module is recommended. ** HubSpot (TAN-2992)** HubSpot data, including contacts and companies, can now be imported based on the lifecycle status. ** Translations (FFU-1901)** All Fulfillment module titles have been translated to the available languages. ** DATEV (FAC-2196)** The export history for DATEV has been improved. ** Kaufland (ECOM-1883)**

A new method to manage new products (EANs) has been added, based on the regulations of Kaufland.

#### Bug fixes **Sales Order (FFU-1647)** Certain foreign letters were displayed as questions mark and not as correct letters. This has been fixed. ** Shopify (ECOM-3347)** Some sales orders could not be imported. This has been fixed. ** Ticket system (TAN-3375)** There was an issue with the ticket forwarding feature where the entire ticket history was being forwarded to the designated mail address. ** Product overview table in NextGen (PIM-1273)** The preview image in the dropdown product preview, as well as on the product edit page, now correctly reflects the latest version of the file, with the sort field being taken into account. ** Mobile warehouse management (FFU-1875)** Under certain circumstances, multiple positions of the same item were not correctly recorded from intermediate storage when using the Mobile warehouse management app. ** Order proposal (FFU-1810)** Filter settings will be retained and the results displayed after reloading the order proposal page. ** Payment transactions (FAC-2133)** Deleting a collective payment advice no longer incorrectly removes credit note relations in other unrelated payment advice documents. ** Receipt of payment (FAC-1678)** Certain unnecessary Paypal transactions are no longer imported to avoid duplicates. ** Article Module (PIM-1374)** The issue of displaying incorrect thumbnails in the product table's preview has been fixed. ** Online Shops (ECOM-3356)** In certain cases, sales orders were not completely synced across various shop connections. This has been fixed. ** Amazon (ECOM-3357)** Some sales orders could not be imported. This has been fixed. ** Amazon (ECOM-3369)**

There have been issues with the creation of invoices when using Amazon VCS where an additional item with ID = 1 has been added. This has been fixed.

## 23.0 Release and Patch Releases

### Patch Version 23.0.58

*Release date: 24-May-2023 *#### Bug fix **NextGen user interface (PIM-1268)** In some modules in the NextGen user interface, the page reloaded after opening it which didn't provide a smooth user experience. This has been fixed. ** Documents (PF-1545)**

Country name is displayed correctly again in documents that are not in German or English language.

### Patch Version 23.0.57

*Release date: 23-May-2023 *#### New feature **NextGen overview tables (PIM-1143)**

In the NextGen user interface, the filtering in the overview data tables has been improved: Applied filters are now visualized at the top of the table and users can delete individual filters right from the visual indicators.

#### Improvements **Ticket module (TAN-3240)** The image handling in the ticket module has been improved: When an image is added to a ticket by drag and drop, it is now automatically resized to fit the editor. ** Emails (TAN-3149)** For Microsoft Office accounts a re-authenticate button has been added in the email detail view. If you encounter a connection error, click the re-authentication button to receive a new access token. ** Product overview table in NextGen (PIM-1306)** In the Product Overview table, the deletion process for a single product has been improved for more consistency and with clear messaging for better user guidance. ** Emails (PF-1500)** The validation rules for email verifications were adjusted to enable more email domains. ** Sales orders (FFU-1924)** Sales orders without a due date and/or without an early payment date caused a validation error in the API. This has been fixed. ** Delivery note API (FFU-1716)** The delivery notes can now be filtered by the status and date via the API. ** Transfers (FFU-1586)** Transfers will now work with modern SFTP servers. ** Transfers (FFU-1547)** You can now import the GLN of a varying delivery address via the transfer module (field name: liefergln). ** Amazon live and VCS payments (FAC-2114)** For Amazon Live and VSC payment imports, we have improved the handling of duplicate imports of payments: Users can now decide whether suspected duplicates should be rejected automatically or displayed as import errors. ** Credit note API (FAC-2053)**

The credit note update API endpoint has been implemented in a beta version.

#### Bug fixes **Hubspot (TAN-3292)** During the export of company data to Hubspot, any conflicts will be logged with a link to the corresponding data object. ** Sales orders (FFU-1932)** The search feature in the sales order table did return results in some cases. This was caused by the shipping method designation being displayed in the table as additional column. This issue has been fixed. ** Returns and goods receipt (FFU-1865)** In some cases, the goods receipt could not be created properly and the goods could not be stored. This has been fixed. ** Shipping labels (FFU-1855)** A proper message is now shown when the credentials for the shipping method are valid and the user wants to create a shipping label. ** Payment transactions (FAC-2153)** The action 'refunding payments' in credit notes doesn't throw errors anymore. ** DATEV (FAC-2139)** For DATEV v500, the Customers and Suppliers CSV export now has the correct file header. ** Mollie (FAC-2128)** When using Mollie as payment method, the outgoing payment from the credit note is now assigned to the Mollie business account correctly. ** Shopify payments (FAC-2106)** In the business account type Shopify, transactions were imported twice, once in status 'in transit' and once in status 'paid'. This has now been fixed. Only transactions with the status 'paid' are imported. ** Invoices (FAC-520)** Overpayment of invoices is now visible in the invoice protocol and with a positive amount in the balance column of the invoices overview page. ** Amazon (ECOM-3264)** In some cases, the old vat services functionality was still applied for the import of Amazon invoices even though the user changed to the new Amazon VCS Service in Xentral. This has been fixed. ** Shopify (ECOM-933)**

Images were exported in the wrong sorting order from Xentral to Shopify. This is now fixed.

#### Removal **DHL Express (FFU-1844)**

The DHL express module has been declared a legacy module and has been removed from new instances.

### Patch Version 23.0.56

*Release date: 16-May-2023 *#### New feature **Hubspot (TAN-2559)**

The Hubspot integration now also synchronizes companies.

#### Improvement **Products in NextGen (PIM-1330)**

If a product is locked, a corresponding label will indicate this in the NextGen product overview table.

#### Bug fix **Mollie (FAC-2128)**

When using Mollie as payment method, the outgoing payment from the credit note is now assigned to the Mollie business account correctly.

### Patch Version 23.0.55

*Release date: 12-May-2023 *#### New feature **Product data table (PIM-1143)**

In the NextGen user interface, the filtering in the overview data tables has been improved: Applied filters are now visualized at the top of the table and users can delete individual filters right from the visual indicators.

#### Improvement **Ticket system (TAN-3240)** The image handling in the ticket module has been improved: When an image is added to a ticket by drag and drop, it is now automatically resized to fit the editor. ** Emails (TAN-3149)** For Office accounts a re-authenticate button has been added in the email detail view. If you encounter a connection error, click the re-authentication button to receive a new access token. ** NextGen (PIM-1306)** In the Product Overview table, the deletion process for a single product has been improved for more consistency and with clear messaging for better user guidance. ** Email verification (PF-1500)** The validation rules for email verifications were adjusted to enable more email domains. ** API (FAC-2053)**

The credit note update API endpoint has been implemented in a beta version.

#### Bug fixes **Ticket system (TAN-3209)** The ticket forwarding has been fixed. You can now forward a ticket with the entire ticket history to a recipient of your choice. ** Live tables (FFU-1787)** In some instances the technical name of the shipping method was displayed in live tables. This was fixed and the shipping method designation is not displayed. ** Number ranges (TAN-3258)** When setting up own number ranges, the button to set up or edit project number ranges was missing. This button is now available again. ** Autoversand (FFU-1903)** Some issues in Autoversand prevented the printing of certain documents and false assignment of the shipping status. This has now been fixed. ** Sales orders/ Shopware (FFU-1841)**

During import of US sales orders via the Shopware 5 importer, the relevant US state was not transferred correctly. This has now been fixed.

#### Removal **DHL Express (FFU-1844)**

The DHL express module was declared a legacy module and was removed from new instances.

### Patch Version 23.0.51

*Release date: 03-May-2023 *#### Improvements **Documents import (TAN-3162)** The process starter for importing documents has been improved so that it runs only if any documents need to be imported and stops after their import. This improves the performance of the process starters and reduces server load. ** Product external numbers (TAN-3144)** The external numbers of products can now be edited directly in the external number module. ** POS (FAC-2051)** In the POS (point of sale) module being used together with Fiskaly, users don't need to add new addresses anymore for values over 200€. ** DATEV (FAC-1939)** DATEV export will now always contain the correct invoice date, as stated on the invoice. The option to select invoices based on date of receipt will now only affect filtering. ** Sales order API (FFU-1617)** Users can now import sales orders via API. ** Transfer module (FFU-1547)**

You can now import the GLN of a varying delivery address via the transfer module (field name: liefergln).

#### Bug fixes **Production (FFU-1852)** In some cases a production did not finish properly when trying to complete it by clicking Store + Complete Production. This has been fixed. ** Shopify payments (FAC-2106)** In the business account type Shopify, transactions were imported twice, once in status 'in transit' and once in status 'paid'. This has now been fixed. Only transactions with the status 'paid' are imported. ** DHL returns (FFU-1857)** For DHL returns, the labels could not be printed and an error message appeared. This has been fixed so that a stand-alone return label can be printed and the customer address from the database is used as a shipper address. ** Goods receipt (FFU-1865)**

In some cases, the goods receipt could not be created properly and the goods could not be stored. This has been fixed.

### Patch Version 23.0.49

*Release date: 26-April.2023 *#### Bug fix **Analytics (XIN-291)**

The BI widgets on the start page were no longer available after the last update. This has been fixed.

### Patch Version 23.0.48

*Release date: 25-April-2023 *#### New feature **Confirmation email for first login (PF-1335)**

In our efforts to improve the security for our customers, we have added email address verification to the login process: Users logging in for the first time will be sent a confirmation link via email. We have enabled this features in version 23.0.47 and all users logging into their Xentral for the first time in version 23.0.47 or higher will receive the confirmation email.

#### Improvements **Invoices (FAC-2034)** Marking an invoice as sent due to the address setting "Always paper invoice" now leads to a corresponding invoice protocol entry. ** Shipping methods (FFU-1551)** A number of translations in the shipping methods user interface have been improved. ** Sales order API (FFU-1682)** The Created At field will now be filled with the current date for new sales orders and with the earliest logged date from the protocol for existing orders. ** Hubspot (TAN-2723)**

In the Hubspot interface, we have extended the mapping by 5 additional fields: State, Fax, Mobile, Salutation, Distribution/Owner.

#### Bug fixes **Financial accounting export (FAC-1956)** In the financial accounting export for accounts, deviating customer numbers are now also considered for deciding whether the contra-account is a customer number. ** POS (FAC-2040)** When the payment method voucher was used in the POS, the field description overlapped the field itself, thus, making the voucher number unreadable. This has been fixed so that the redeem voucher popup works again in POS. ** DATEV (FAC-2083)** In rare cases updates failed when there were double entries of DATEV exports. This has been fixed. ** Shipping labels (FFU-1797)**

In very rare cases, the creation of a shipping label for a delivery note failed with a 500 error. This has been fixed.

### Patch Version 23.0.46

*Release date: 21-April-2023 *#### Bug fix **Shopify (ECOM-3228, ECOM-3220)**

An issue with stock synching in Shopify has been fixed.

### Patch Version 23.0.44

*Release date: 20-April-2023 *#### Bug fix **Business accounts (FAC-2079)**

When more than one business account was available, payments were posted randomly on any one of them. This has been fixed so that payments are now posted on the correct business account.

### Patch Version 23.0.43

*Release date: 18-April-2023 *#### New features **Personal access tokens (PF-1274)** We have improved the Personal Access Tokens page and created a dedicated section for tokens used by Xentral apps that require access to the Xentral API. ** DHL 3.0 (FFU-898)**

For DHL 3.0, if users select the "print return label with shipping label" option, they can now print the return label together with the shipping label.

#### Improvement **NextGen product table (PIM-1140)**

In the NextGen design, the data overview tables have been improved: A preview is now accessible on the left side of each row, and available actions are now always visible on the right side of each row.

#### Bug fixes **Import templates (TAN-2896)** All users with appropriate permissions are now able to upload CSV import files in the Import Template module. ** Employee vacation schedule (TAN-2889)** In Employee Administration, the Vacation Schedule (all employees) calendar was missing for the year 2023. This has been fixed. ** Sales orders (FFU-1636)** The sales order status section with the status indicators was missing from the quick preview of a sales order. This has been fixed so that the statuses will now appear in the quick preview. ** Dropshipping warehouse (FFU-1464)**

In some cases, dropshipping orders were not split into the correct number of partial orders, but extra empty orders were created. This has been fixed.

### Patch Version 23.0.42

*Release date: 13-April-2023 *#### Bug fix **DATEV (FAC-2062)**

Due to an issue with the login to DATEV, exports to DATEV failed in version 23.0.41. The underlying issue with the creation of login data has been fixed.

### Patch Version 23.0.41

*Release date: 12-April-2023 *#### Improvements **Products (PIM-1141)** In the data tables in NextGen design, we have improved the position and order of actions such as filters and search bars based on customer feedback. ** Amazon (ECOM-1902)**

We now support more than one SKU for Amazon FBM listings.

#### Bug fixes **Products (PIM-1037)** In the NextGen design, the preview of product images did not display the correct image, but a random image or just a background. This has been fixed. ** Shipping methods (FFU-1661)** In the Shipping Method Details page in the Expert Settings section, when Shipping Mail to Buyer was set to CustomText Template, users could not select and save a specific template in the Text Template field. After saving it was reset to the default template. This has been fixed. ** Extended approval (FFU-1660)** In a multi-stage approval process for receipts, users could not select the correct approver from the corresponding drop-down list because the drop-down list was empty. This has been fixed. ** FinAPI (FAC-1985)** In the NextGen design, the FinAPI login now works properly again. ** DATEV Connect (FAC-1531)** In the DATEV Connect module, the login to Datev works again in the new design. ** Bookings (FAC-867)**

In bookings the deviating customer number from the underlying document is now taken into consideration, not only the number from the contact.

### Patch Version 23.0.40

*Release date: 06-April-2023 *#### Bug fix **Cash register (FAC-2047)**

After an update to version 23.0.38, it was not possible to save new bookings, carry out cashier closing, or view the current bookings in the cash register module. This has been fixed.

### Patch Version 23.0.39

*Release date: 06-April-2023 *#### Bug fix **Shopify Business Operations app (ECOM-1903)**

Due to the use of deprecated API calls in the background, the connection between Xentral and the Shopify Business Operations App did not work properly, e.g. in conjunction with credit notes. This has been fixed.

### Patch Version 23.0.38

*Release date: 04-April-2023 *#### New feature **DHL 3.0 (FFU-871)**

We implemented an endpoint for the DHL Returns API.

#### Improvements **PHP upgrade (FAC-2019)** The following modules have been made ready for PHP 8.1: receipts import, alcohol tax calculator and POS scanning. ** PHP upgrade (FAC-1944)** The cash registers module is now ready for PHP 8.1. ** PHP upgrade (FAC-1886)** The HBCI accounts module is now ready for PHP 8.1. ** Export of invoices and credit notes (FAC-1821)** We have improved the performance of CSV and XML exports for invoices and credit notes in order to avoid timeouts or very long runtimes. ** Amazon (ECOM-1819)** We have introduced a Get Token button in the Amazon Configuration that allows users to create or renew the Amazon Seller Central token. ** Shopify (ECOM-1739)** Xentral now supports the new Shopify Meta Field API (2023-01). ** Sales order API (FFU-1662)**

The Sales Order List endpoint can now be filtered by status.

#### Bug fixes **Accounts (FAC-1845)** We have removed the payment details from invoice documents when the payment is done via Mollie. ** Check boxes (FAC-1887)** In invoices and liabilities that were set to read-only, some check boxes that users should still be able to select or clear were insensitive. They are now clickable again. ** Mollie (FAC-1987)** In the NextGen user interface, users could not access the Mollie account settings. This has been fixed. ** Invoice run (FAC-2013)** The subscription cycle forecast with type "once" will not displayed multiple times anymore. ** DATEV (FAC-2029)** There was an issue when a legacy system has more than one set of DATEV settings with the same project ID. ** POS (FAC-2036)** A discounted position will not be shown in the POS receipt anymore if the value is 0 Euro. ** Delivery note (FFU-1723)**

There have been issues with the quick preview of delivery notes. This issue has been fixed.

### Patch Version 23.0.37

*Release date: 29-March-2023 *#### Bug fix **Process starters (FFU-1767)**

The process starter "lagerzahlen" did not sync stock numbers to sales channels anymore. This has been fixed.

### Patch Version 23.0.36

*Release date: 29-March-2023 *#### Bug fix **Liabilities (FAC-2006)**

The export of liabilities to DATEV resulted in an error when the invoice date was empty. This has been fixed.

### Patch Version 23.0.35

*Release date: 28-March-2023 *#### Improvements **Payment transactions (FAC-1948)** We have ensured the payment transactions module's readiness for PHP 8.1. ** DATEV (FAC-1939)** DATEV export will now always contain the correct invoice date, as stated on the invoice. The option to select invoices based on date of receipt will now only affect filtering. ** Reports (FAC-1800)** The old report module will now be excluded from the super search to avoid two report modules in the search results. ** Sales order API (FFU-1691)**

The shipping address object will be filled with the billing address, if no alternate shipping address was specified.

#### Bug fixes **Shipping methods (FFU-1696)** The "No dispatch mail" setting was not saved in the "Shipping mail to buyer" field, but it was reset to "Custom text template" instead. This has been fixed so that "No dispatch mail" can be saved and is applied successfully. ** Product master data (FFU-1588)** After an item with a serial number has been retrieved from stock, the corresponding serial number does not disappear from the "in stock" tab in the product master data which in consequence leads to an error message due to too many serial numbers being shown. This has been fixed so that serial numbers of retrieved items now properly disappear from the "in stock" tab. ** Payment transactions (FAC-1831)** A SEPA XML file created via the payment transaction module now contains both purpose lines. ** FTP Backup (CCS-111, CCS-153)**

We have fixed issues with the FTP Backup module for cloud customers.

### Patch Version 23.0.34

*Release date: 24-March-2023 *#### Bug fix **Feature flag (PF-1370)**

Due to a missed feature flag, several customers on 23.0.33 saw a feature that was not yet ready in their instances. This hotfix resolves that issue.

### Patch Version 23.0.33

*Release date: 23-March-2023 *#### Bug fix **Price inquiries (FFU-1743)**

Statuses were not properly assigned to price inquiries. Thus, it was not possible to approve price inquiries. This has been fixed.

### Patch Version 23.0.32

*Release date: 22-March-2023 *#### Bug fix **DATEV (FAC-1993)**

DATEV UO (Unternehmen Online) exports were blocked for on-premise customers. This has been fixed.

### Patch Version 23.0.31

*Release date: 21-March-2023 *#### Bug fix **DATEV (FAC-1970)**

When running a DATEV UO export, an error message was displayed to on-prem customers. This has now been fixed.

### Patch Version 23.0.30

*Release date: 21-March-2023 *#### Improvements **Products (PIM-1176)** The product cache has been optimized leading to overall performance improvements of product related requests. ** NextGen (PIM-1169)** In the Products table in the NextGen user interface, we have now introduced a visual indication for products that are locked. ** Sales order API (FFU-1671)** We have streamlined the statuses in the sales order API's LIST and VIEW endpoints to be consistent with other document types like invoices. ** Sales order API (FFU-1631)** We have improved the structure of the LIST and GET endpoints for sales orders. ** DATEV (FAC-1920)** The login process for DATEV Connect has been improved so that fewer exceptions will now occur during the login: The expiration date of the refresh token is now handled properly. ** Invoices (FAC-1304)**

When creating an invoice, if the selected customer is assigned to a project, then the project VAT ID will now be used as Own-VAT ID, as long there is no delivery threshold configured.

#### Bug fixes **Import template (TAN-2959)** Target drop-down in import template shows currently selected value. ** Klarna (FAC-1973)** Business accounts based on Klarna can now import transactions again. ** DATEV (FAC-1959)** In cases when two liabilities have the same invoice number, the PDF is now also exported correctly as part of an XML-based financial export. ** Payment advice (FAC-1957)** The cronjob that sends out payment advices has been fixed and now works properly. ** DATEV (FAC-1955)** In DATEV exports, very long error messages in the URL led to a gateway error. This has been fixed. ** Pick lists (FFU-1664)**

In some cases not all sales orders containing JIT products ready for shipping were shown in the pick list module. This has been fixed.

### Patch Version 23.0.29

*Release date: 14-March-2023 *#### Bug fix **Shop importer (ECOM-1814)**

The Settings for Shop or Marketplace section was missing on the Interface tab of the shop importer's Details page. This has been fixed.

### Patch Version 23.0.27

*Release date: 14-March-2023 *#### New features **Webhooks (PIM-1091)** You can now subscribe to an event, that will be generated whenever a product is created, using webhooks. ** Amazon (AMAZON-1898)**

In the Amazon shop importer settings, the legacy settings of the old VCS implementation are now hidden by default. If needed, they can be displayed by clicking the corresponding check box.

#### Improvements **API (PIM-1096)** External developers can now create, read, update, and delete a product's purchase prices via the API. ** Performance (FFU-1596)** The performance of the Lagerzahlen cronjob has been improved. ** Country list and states modules (FAC-1869)** The Country List module and the States module will be removed in the future. As a first step, we have deactivated all create, edit and delete options. ** Shopify API (ECOM-1802)** We have added pagination support for the GraphQL Shopify API to our Importer. ** Shopify POS (ECOM-1526)** We have improved the error handling for the sales order import of Shopify POS sales orders. ** New Xentral updater (PF-1228)**

All new Xentral instances are now using the new Xentral updater. It has some minor user interface changes, but most importantly it makes the updates faster and more stable.

#### Bug fixes **User interface (PIM-1173)** When using Xentral on a mobile device, parts of the sidebar navigation (administration menu) weren't accessible at all times. This issue has been fixed. ** Picking list (FFU-1651)** With the Picking list details module active, the sorting order in the pick list was not correct. This has been fixed. ** DHL 3.0 (FFU-1579)** Printing a shipping label automatically as part of step 1 of the auo-shipping process with DHL 3.0 failed in specific cases. This has been fixed. ** Dispatch center (FFU-1521)** The filtering of the delivery note field in the Shipped tab of the dispatch center now shows proper results. ** Datev connect (FAC-1899)** In DatevConnect there will now be fewer exceptions caused by invalid login data. ** Credit notes (FAC-1640)** If a customer tries to split an incoming payment and selects the type credit note, this type is now also prefilled correctly on the incoming payment page. ** Payment methods (FAC-982)** User-generated translations in the payment methods module now work again. ** Dispatch center (FFU-1687, FFU-1685)** Scanning of batches in dispatch center is now stocking out the correct number of best-before stock from correct storage location. ** Batches (FFU-1678)**

The "autoversand_manuell" cronjob will not crash anymore when the batches app is active.

### Patch Version 23.0.26

*Release date: 07-March-2023 *#### Bug fix **Amazon FBM stock sync (AMAZON-1955)**

An issue with the update of Amazon FBM stock information from Xentral to Amazon via the SP-API has been fixed so that the Amazon FBM stock sync now works again properly.

### Patch Version 23.0.25

*Release date: 07-March-2023 *#### Improvements **Direct debit (FAC-1862)** The IBAN in the payment advice has been anonymized in accordance with GDPR rules. ** Shopify payments (FAC-994)**

We have improved the receipt of payment Shopify live import.

#### Bug fixes **Sales order (FFU-1583)** The quick overview in the Delivery Handover tab of the Sales Order module displayed incorrect data. This has been fixed. ** Formulas (FFU-1582)** In rare cases formulas acted upon the wrong items and therefore the wrong calculated numbers were displayed in documents. This issue happened only under specific circumstances involving parts lists, disabled listing of items documents, and formulas that act upon these items in documents. This has been fixed. ** Delivery notes (FFU-1542)** Postage items were not displayed on delivery notes even though the Only take over stocks items (Nur Lagerartikel übernehmen) setting in Projects was not selected. This has been fixed. ** Dispatch center (FFU-1468)** Proper error messages have been added when users scan invalid delivery notes, e.g. because the delivery note does not exist or was cancelled. In particular, there is now a proper error message when a user tries to scan a delivery note a second time that has already been processed. ** Receipt of payment (FAC-1853)** In some cases, there was an error in the background with the quick preview. ** Liabilities (FAC-1846)** When different suppliers used the same invoice number, these liabilities could not be exported into DATEV. This has been fixed. ** Reports (FAC-1827)** The "083 - customers who have not ordered anything for X days" report now delivers correct data. ** Shipping tax split (FAC-1781)** The shipping tax split module doesn't calculate anything if you add a shipping position manually and the checkbox for automatic calculation is not active. ** Taxdoo (FAC-1756)** All documents are now transmitted properly to Taxdoo in accordance with the document date in UTC. ** Payment advice (FAC-1650)**

The payment advice now uses the same document background as the underlying invoices based on their projects.

### Patch Version 23.0.24

*Release date: 03-March-2023 *#### Improvements **NextGen user interface (GRO-196)** We have changed the German names and positions of some tiles in the NextGen launchpad. ** Shop export (ECOM-1346)**

Even if only the price of an item has changed, this will now be updated in the online shop.

#### Bug fix **Amazon (AMAZON-1946)**

The difference between FBA and FBM stock updates was not properly respected in the Amazon shop interface and the stock was updated for both FBA and FBM. This has been fixed so that now only stock for FBM listings is updated.

### Patch Version 23.0.22

*Release date: 01-March-2023 *#### Bug fix **Invoices (FAC-1859)**

The quick preview of an invoice in the Invoices overview table (when expanding the invoice or clicking on the invoice number in the table) displayed a wrong invoice, whereas in Edit mode the correct invoice was displayed. This has been fixed so that the correct invoice is now displayed in all cases.

### Patch Version 23.0.21

*Release date: 28-February-2023 *#### Improvements **Shipping method: Amazon Prime (FFU-1452)** We removed the fields to connect the Amazon Prime shipping method via Amazon MWS as this method of connection is no longer functional. ** Shipping methods (FFU-1015)** The settings for the shipping methods GLS, DPD, and DHL (alt) are now divided into basic and expert settings. ** Shipping methods (FFU-662)** When copying a shipping method, problems could arise because of duplicate types. If you copy a shipping method now, a unique entry for type will be generated when you save. ** Split shipping (FAC-1007)** The Update postions button no longer has an effect on items that are marked as postage, because this could cause issues with postage items that were changed by the Split shipping module. ** Credit notes API (FAC-1824)** We created an API endpoint that is able to deliver all related documents for a specific credit note. This endpoint is currently in Beta. ** Kaufland (ECOM-1665)** You can now map all your product listings in Kaufland with one single table based on EAN codes. ** Kaufland (ECOM-1664)**

You can now select a product category to export your products with the new Kaufland API 2.0.

#### Bug fixes **NextGen user interface (PIM-1168)** We have fixed several issues with the Back button in Xentral NextGen. ** Production (FFU-1630)** When adding a batch to production, an error message appeared. This has now been fixed. ** Order proposal (FFU-1623)**

When users tried to open the product overview tab in the Order Proposal module, an error message appeared due to wrong formatting quantities internally. This has been fixed.

### Patch Version 23.0.20

*Release date: 23-February-2023 *#### Bug fix **Tracking numbers (FFU-1612, FFU-1606)**

A 500 error message ("Undefined class constant DOCUMENT_INVOICE") appeared when users tried to save the tracking number from the shipping provider. The underlying issue has been fixed.

### Patch Version 23.0.19

*Release date: 21-February-2023 *#### New feature **DHL. 3.0 (FFU-810)**

For DHL 3.0, the visual age check feature is now available.

#### Improvements **Contacts (TAN-2899)** The user interface in the Addressfilter module is now available in English as well. ** Product API (PIM-1095)** External developers can now create, read, update, and delete product properties via the API. ** Revenue statistics (FAC-1761)** In the revenue statistics, the revenue is now split by currency so that different currencies are not added up anymore. ** Credit note API (FAC-1735)** We have added the "Get Credit Note" details endpoint that allows getting comprehensive data of a credit note via API. ** Liabilities (FAC-866)** The project field in liabilities is now filled automatically with the preferred project or, if there is no preferred project, with the default project. ** DATEV (FAC-210)**

The email is now exported to DATEV together with the other data in the manual customer/supplier CSV export.

#### Bug fixes **Pipedrive (TAN-1982)** The Pipedrive integration has been fixed. Contacts and deals can be synchronized between Xentral and Pipedrive. ** Internetmarke shipping label (FFU-1581)**

The issue with creating Internetmarke shipping labels has been fixed.

### Patch Version 23.0.18

*Release date: 16-February-2023 *#### Bug fixes **Kaufland (ECOM-1744)** The order import from Kaufland to Xentral failed. This has been fixed. ** Kaufland (ECOM-1747)**

If the Kaufland shop importer interface was set up with wrong or missing credentials, all products linked to this online shop could not be edited anymore in Xentral. This has been fixed.

### Patch Version 23.0.17

*Release date: 16-February-2023 *#### Bug fix **DATEV (FAC-1805)**

The DATEV Rechnungsdatenservice (formerly DATEV connect online) module was not visible and not usable in some Xentral instances. This has been fixed.

### Patch Version 23.0.16

*Release date: 14-February-2023 *#### Improvement **Personal access tokens (PF-1015)**

The functionality of the personal access tokens has been extended so that they are now available for older Xentral APIs as well. Please keep in mind that the permissions of the old APIs do not apply when you use the personal access tokens.

#### Bug fixes **Projects (FFU-1470)** We have fixed an issue with attachments in connection with the auto-shipping option. ** Production (FFU-1367)** When an item that was part of a production parts list was located in two warehouses with the same batch number and best before date, it was not retrieved from the preferred warehouse, but from the warehouse with the most stock instead. This has been fixed, so that now the preferred warehouse will be used. ** Management board (FAC-1783)**

In the Management board, the Liabilities (gross) fields for the previous months now properly sum up all liability amounts - no matter whether they have been paid or not.

### Patch Version 23.0.15

*Release date: 09-February-2023 *#### Bug fixes **Shopimporter (ECOM-1736)**

Orders from shops and marketplaces were only imported into the intermediate table and needed to be imported manually. This was fixed and the process is fully automated again and the intended behavior restored.

### Patch Version 23.0.14

*Release date: 08-February-2023 *#### Bug fixes **Financial accounting export (FAC-1149)** We fixed an issue where the liabilities number in the file name was incorrectly exported from DATEV. ** Hubspot (TAN-2958)**

We fixed an issue where Hubspot users could not properly update their Xentral instance.

### Patch Version 23.0.13

*Release date: 07-February-2023 *#### New feature **Email account (TAN-2893)** If you added a specific email address in both the basic settings and the Email accounts module,Xentral will use the configuration from the Email accounts module. ** Important**: In this case make sure that you have defined your SMTP settings in the Email accounts module, as you will not be able to send emails from Xentral otherwise.

We updated the default PHP Mailer to the latest version.

#### Improvements **Financial accounting export (FAC-1694)** We now show an error message if there is an error while creating a PDF during the financial accounting export. The error message displays a link to the respective document. ** Translations (FFU-1430)** We have added some missing translations to the user interface of the sales order positions table. ** Translations (FFU-1527)** We have added some missing translations to the user interface of sales orders and delivery notes. ** Hubspot (TAN-2799)** There was an error, when too many requests were sent to the Hubspot API. This issue has been fixed. ** Products API (PIM-1065)** Users can now create, read, and update more parameters among the product details via the Xentral API. ** Products API (PIM-1066)** Users can now create, read, and update product sales prices via the API. ** Sales order API (FFU-1415)** We added data for sales order items to the GET endpoint. ** DPD AT (FAC-1471)**

The tracking number is saved automatically against the shipping label for DPD AT.

#### Bug fixes **Split shipping (FAC-1150)** When you use split shipping, float tax rates, like 5.5, are now used in the correct way and the shipping articles are generated correctly. ** Receipt of payment (FAC-1617)** Klarna transactions can now be properly matched to the corresponding document. ** NextGen overview tables (PIM-1027)** A filter setting applied to one overview table was also applied to other overview tables erroneously. This has been fixed. ** Tags (PIM-1042)** The color scheme of tags in the NextGen and classic design have been aligned. ** User management (TAN-2180)**

The permission for editing payment transaction now works correctly.

### Patch Version 23.0.12

*Release date: 31-January-2023 *#### Improvements **Payment transactions (FAC-1716)** The direct debit avise PDF now displays the amount (in the description text of the avise) with two decimal places. ** Sales order API (FFU-1403)**

Users can now specify order date from and until, so that only orders in a specified date range are reported.

#### Bug fixes **Financial accounting export (FAC-1691)** Special characters such as "&" in the document field (Belegfeld) cause problems when you export liabilities with DATEV. These characters now automatically get excluded/replaced. ** Invoices (PIM-1029)** When you clicked on the filter button in the invoice table using the NextGen design, you got an error message. This issue has been fixed. ** Translations (TAN-2616)**

We have fixed some language issues with user interface labels in the User module.

### Patch Version 23.0.11

*Release date: 30-January-2023*

#### Bug fix

We have added digital signature functionality to all relevant eBay calls to meet new security verification requirements.

### Patch Version 23.0.10

*Release date: 24-January-2023 *#### New feature **Shipping methods (FFU-1126)**

Shipping labels are now stored in the Files section of the sales order and of the delivery note for later use, for example, to print the label again.

#### Improvements **API (PIM-1011)** Users can now delete products via the API. ** API (PIM-945)**

The Update Product endpoint has been enhanced in scope so that more product fields can now be updated.

#### Bug fixes **NextGen user interface (PIM-1044)** Some issues with login to Xentral NextGenhave been fixed. For example, user trying to go to sales orders were asked to enter login credentials again. ** Products (PIM-993)** If the selling price in a product had been defined in a currency other than the default currency, and this product was added to an offer or sales order, the selling price did not appear in the document. This has been fixed. ** Liabilities (FAC-1670)** Liabilities with correct goods and invoice inspection are not indicated as "not loadable" anymore when imported in the payment transactions module. ** Payment methods (FAC-1656)** The creation of new payment methods (by clicking +NEW) except for the "custom" payment method was not possible. This has been fixed. ** Payment transaction (FAC-1637)**

The correct number of payments is now displayed in the Payments tab again.

### Patch Version 23.0.8

*Release date: 23-January-2023*

#### Improvement

We have added the Ebay header signature on all finance requests so that we can ensure compliance with Ebay from next month onward. This is still hidden behind a feature flag at the moment.

### Patch Version 23.0.7

*Release date: 20-January-2023 *#### Bug fix **Shipping methods (FFU-1428)**

Custom carriers (shipping method "Custom") were unavailable after an update to version 23.0.4. This has been fixed.

### Patch Version 23.0.6

*Release date: 19-January-2023*

#### Bug fix

Reports did not load and the corresponding activity indicator (the spinning Xentral icon) was visible indefinitely. This has been fixed.

### Patch Version 23.0.5

*Release date: 19-January-2023*

#### Bug fix

We have restored functionality of the dispatch center with regards to batches, (manual) auto-shipping, and auto-shipping plus.

### Patch Version 23.0.4

*Release date: 18-January-2023*

#### Bug fix

Printing shipping labels in stage one of the logistics process did not work properly. A few issues in this context have been fixed.

### Patch Version 23.0.3

*Release date: 17-January-2023 *#### Improvements **NextGen user interface (PIM-1032)** We have changed the color of links in system messages pointing to other resources, e.g. to sales orders or invoices, in order to improve readability. ** Liabilities (FAC-1669)**

The status of a liability is set back to "open" after a partial payment (bank transaction) has been removed from the liability.

#### Bug fixes **App Store (PIM-1024)** In the NextGen user interface, users could not open apps from the App Store: After clicking on the app's open button, an error message appeared. This has been fixed so that the apps are now accessible. ** Fiskaly (FAC-1687)** The transactions tab in the Fiskaly module did not display entries also with large amounts of data. This has been fixed. ** NextGen user interface (PIM-1007)** When a user filtered a table (e.g., the Products table) in the NextGen user interface and then reloaded the page, the filter was still shown as applied, but the table was not filtered anymore. This has been fixed so that the filter is still applied after reloading the page. ** Liabilities (FAC-1633)** In the incoming payments module, liabilities match to the bank transactions by their document number again. ** Payment transactions (FAC-1513)** The error message on Accounting > Payment transactions > Direct debits > SEPA collective debits has been removed and printing works again. ** Sales orders, invoices, and delivery notes (FHPB-12)** Sales prices in other currencies than the standard currency in the system were not applied correctly in sales orders, invoices, and delivery notes: Instead of the actual price in the non-standard currency being directly applied, the conversion rate was applied again on the price, thus resulting in a wrong price in the document. This has been fixed. ** Pipedrive (TAN-1982)**

Pipedrive did not sync properly and an error message did not disappear in conjunction with the setup of free fields. This has been fixed.

### Patch version 23.0.2

*Release date: 13-January-2023*

This version contains no changes compared to the previous version. We have created this version for technical reasons.

### Patch Version 23.0.1

*Release date: 11-January-2023 *#### Bug fix **finAPI (FAC-1693)**

Customers using the live banking connection via finAPI were unable to renew their bank consent due to a synchronization issue between Xentral and finAPI.

### Release Version 23.0.0

*Release date: 10-January-2023 *#### New feature **Mobile version (PIM-768)**

The app's homepage has been optimized for mobile devices.

#### Improvements **Service order (FFU-1273)** The service order module is now available in new instances again. ** Shopify POS (ECOM-1528)** If a sales order is imported into Xentral from Shopify POS that has no other customer data than an email address (in particular, no first and last name), the customer data is now overwritten with the default customer - otherwise,Xentral would ignore the sales order. ** NextGen user interface (PIM-772)** Your subscription status is now displayed in the side menu. ** Dispatch center (FFU-1120)** We improved the loading times when users scan items in the dispatch center. ** DHL 3.0 and Sendcloud (FHPB-2)** It is now possible to create shipping labels for item quantities less than 1. ** Financial accounting export (FAC-586)** Concatenated account and booking key number having been manually inserted in the bank transaction by the user will be checked against the customer number in the accounting export. This will prevent that these values aren't split in the export. ** API (PIM-840)**

The Create Product endpoint is now available in the XentralAPI.

#### Bug fixes **Purchase orders (FHPB-15)** When a purchase order with a non-default taxation was edited, the taxation reverted back to the default setting. This has been fixed. ** Online shops (ECOM-1630)** Some customers reported issues after the update to version 22.5.3 when they checked the connection to the online shop or when they picked up sales orders manually in the shop importer. The database connection errors for several shop interfaced have been fixed. ** Employee time tracking (TAN-2767)** The vacation day settings for the year 2023 are now possible. ** Documents (sales order, proposal, delivery note, invoice) (FHPB-3)** When a user changed or added the contact data directly in the document instead of retrieving it from the master data, the contact's state and country were not applied. ** Financial accounting export (FAC-1623)** The export button in the DATEV financial export module works again. ** Sendcloud and DHL 3.0 (FFU-1279)** If discount items were part of a sales order, the shipping labels were not created properly. The bug fix leaves out discount items from shipping label requests. ** NextGen overview tables (PIM-935)** A bug with the overview tables in the Xentral NextGendesign has been fixed: You can now sort columns alphabetically in ascending and descending order. ** FinAPI (FAC-1612)** If the bank connected to FinApi requires a renewal of credentials, you will now see a message in the account and on the payment transaction import page. ** Returns (FFU-1104)** The link to the help center in the return order module has been fixed. ** Delivery notes (FHPB-16)** The CN23 form used to have all items from the invoice instead of only the items from the delivery note. This has been fixed. ** Sales orders (FFU-1064)** Special line items (such as group headings) in the sales orders used to have wrong denominations and could not be deleted. This has been fixed. ** Warehouse (FFU-977)** Under specific conditions, when items with serial numbers were relocated, the serial number remained with the old storage location instead of moving with the items. This has been fixed. ** Delivery notes (FHPB-4)** The selected delivery date was not saved when an item was added to the purchase order. This has been fixed. ** Delivery note (FHPB-10)** Batch items were incorrectly put back into stock after the cancellation of a delivery note. ** Warehouse (FHPB-38)** When you tried to store items with serial numbers, clicking on the Serial Number Assistant button did not open any wizard. ** Tasks (FHPB-5)** Special characters are now displayed correctly on a task's PDF. ** Amazon (FAC-767)**

The tax rate on the invoices and sales orders was different from the tax rate on the Amazon invoice. This has been fixed.

## Frühere Versionen

Du kannst die Release Notes für frühere Versionen[hier](https://help.xentral.com/hc/de/articles/4409075372828#UUID-a3b0a08c-9ea7-2c75-a117-c14e87fbe1bc)ansehen.