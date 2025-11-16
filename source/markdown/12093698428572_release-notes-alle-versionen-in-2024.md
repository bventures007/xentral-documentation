## 24.21 Release and Patch Releases

### Release Version 24.21.3

*Release date: 04-June-2024 *#### New feature **New Analytics module**

Implemented the second alpha version of the new Analytics module. This early version of the feature is only available on selected instances.

#### Improvement **DHL (FFU-2240)** DHL Versenden has been updated to the newer version of the SOAP API (V2) to ensure continued functionality for international deliveries after May 31st. ** Accounting Export V2 (FAC-3215)**

Clarification (outgoing) account added to the PayPal provider in Accounting Export V2 module.

#### Bug fixes **Transfers (FFU-3447)** Encoding issues when importing CSV files via TransferSmarty have been resolved. ** UPS OAuth (FFU-3387)** Shipping to Mexico now works when using the UPS OAuth shipping method. ** Sales Order Import API (FFU-3380)** Comments in position payloads are now persistently aligned with API documentation specifications. ** API (FFU-3041)** API-generated tracking information now accurately includes carrier details. ** UPS OAuth (FFU-2884)** Creating shipping labels for the US now works when using the UPS OAuth shipping method. ** Accounts: PayPal (FAC-3012)** PayPal transactions which are not part of the detailed list provided by the PayPal API (like currency conversions and fee reversals) can now be imported as well. This feature is under Feature Flag and not available to every customer. ** Financial accounting export (FAC-2478)** Outgoing payments are now also taken into consideration to enrich data needed for DATEV exports, even for invoices. ** Payment transactions (FAC-2286)** Direct Debits will now be automatically selected for export 10 days before their Due Date, thus providing the bank with enough time to complete the transaction on the Due Date. The SEPA Required Collection Date will be directly filled in by the Due Date, removing hard coded date calculation logic. ** Shopware 6 (ECOM-4310)** Resolved an issue that prevented image upload to Shopware 6.5.8.9. ** Amazon (ECOM-4166)** An error which can cause Amazon B2B orders to not have a VAT ID has been fixed. ** Amazon Seller App (ECOM-4164)**

Resolved an issue where the Amazon Seller App synched stock from Amazon even though external item number (Fremdnummer) mappings have been removed. This was caused by products with an identical product SKU and Amazon SKU.

## 24.20 Release and Patch Releases

### Patch Version 24.20.3

*Release date: 29-May-2024 *#### New feature **UPS (FFU-2764)**

The Paperless Invoice feature has been added for UPS.

#### Improvement **DHL (FFU-2240)**

DHL Versenden has been updated to the newer version of the SOAP API (V2) to ensure continued functionality for international deliveries after May 31st.

#### Bug fix **UPS (FFU-3387, FFU-2884)** Shipping parcels to Mexico using UPS could not be completed due to a missing merchandise description field. This has been fixed. The US state/province is now shown on shipping labels. ** UPS (FFU-2884)**

Creating shipping labels for the US using the UPS OAuth shipping method was not functioning properly. This issue has been resolved, and labels can now be generated successfully.

### Release Version 24.20.2

*Release date: 29-May-2024 *#### New feature **API (FAC-3199)**

A document number can now be added when creating an invoice or credit note via the API.

#### Improvement **Mobile Warehouse Management (FFU-3248)**

The redirect process after changing stock has been improved for better efficiency.

#### Bug fixes **Backend (PF-2572)** Fixed an issue that prevented some customers from logging into their instance. ** Post.AT (FFU-3278)** Cash on Delivery now functions correctly for the shipping method Post.AT. ** Delivery Note (FFU-3261)** An error message is now displayed if there is insufficient stock to retrieve. ** Shipping Center (FFU-3225)** Partial delivery notes created in the shipping center are now marked as sent. ** Serial Numbers (FFU-2618)**

Returned items with serial numbers are no longer shown to be at the customer.

## 24.19 Release and Patch Releases

### Release Version 24.19.3

*Release date: 27-May-2024 *#### Bug fix **Backend (PF-2572)**

Fixed an issue that prevented some customers from logging into their instance.

### Release Version 24.19.2

*Release date: 21-May-2024 *#### Improvements **Purchase Order API (FFU-2918)** Implemented an API endpoint for releasing purchase orders. ** Referral programme (GRO-560)**

The customer referral programme is now also available from classic design.

#### Bug fixes **Amazon (ECOM-4266)** Amazon sales order import having discounts associated with specific items in the sales order will not cause the discounts to have the wrong taxation any longer. ** Shopify (ECOM-4292)** Resolved an issue with escaping data in logs on the settings page. ** Onlineshops (ECOM-4325)** In the shop importer settings, various tabs like payment methods, shipping methods, freefields, etc. were not displaying any content. The configuration tabs have been restored. ** Article (PIM-2214)**

On the product details page, the browser incorrectly asked for confirmation to leave the page when no changes were made. This has been fixed.

## 24.18 Release and Patch Releases

### Release Version 24.18.1

*Release date: 14-May-2024 *#### New feature **Accounting Export V2 (FAC-2797)**

A new module that will form the basis of a complete overhaul of both the payment import and export processes in Xentral. This first iteration focuses on the export of PayPal transactions to the DATEV CSV format.

#### Improvements **Liability API (TAN-4456)** A GET list of liabilities endpoint has been added. Further information can be found on developer.xentral.com. ** Purchase order API (FFU-2924)**

The Patch /api/purchaseOrder/[id] is now available as an early access endpoint.

#### Bug fix **eBay (ECOM-4268)**

The stock sync now works correctly for products with a high number of variants.

## 24.17 Release and Patch Releases

### Patch Version 24.17.3

*Release date: 07-May-2024 *#### Bug fix **Backend (SRE-2086)**

Resolved an issue with the update process for instances that use automatic updates.

### Release Version 24.17.2

*Release date: 07-May-2024 *#### Improvements **Email Log (TAN-4539)** The email log got a new icon and was moved from the Warehouse to the Team section. ** Customer API (TAN-4405)** Increased the performance of the list endpoint for systems with large amounts of data. ** Financial accounting export (FAC-3108)** All of the available export formats for Xentral Invoices (DATEV CSV, DATEV XML, Rechnungsdatenservice 1.0) will now contain the invoice "Due Date". ** Amazon (ECOM-4254)**

Amazon settings have been rearranged: VCS settings have been grouped, the gift product option for the new VCS mechanic has been removed as a dedicated gift product option already exist in the settings, and the "Automatically add gift product option" has been removed as the functionality is not required.

#### Bug fixes **Gmail (TAN-4543)** Resolved an issue with authentication via token when connecting to Gmail that blocked the dispatch of emails. ** Customer API (TAN-4514)** When creating a new customer via the API, the project is now correctly set with the request data provided. ** Shipping method (PIM-2192)** Missing English translations added for shipping method configuration. ** NextGen user interface (PIM-2170)** Fixed an issue where part of the interface would show in German and part of the interface would show in English after leaving the app idle for multiple hours. ** Import template (PIM-2157)** The "hinweis_einfuegen" variable can now be used in an initial import of products as well as in updates. ** SmartSearch (PIM-2147)** Resources with dashes and underscores can now be found through SmartSearch. ** TransferSmarty (FFU-3183)** It is now possible to convert ISO-8859-1 files with special chars in TransferSmarty-account. ** Dropshipping warehouse (FFU-3054)** Auto-shipping is now enabled for sales orders split into partial shipments. ** Commission agent (FAC-3181)** The commission rates for credit notes are now correctly calculated, when different rates are applied to item categories. ** Subscription run (FAC-3081)** A mechanism to prevent duplicate execution of subscription runs has been implemented. ** Amazon (ECOM-3808)**

Amazon order import will no longer create sales orders which have the street name copied into the department.

#### Removal **US taxes (PF-2402)**

The US taxes module has been removed.

## 24.16 Release and Patch Releases

### Patch Version 24.16.3

*Release date: 30-April-2024 *#### Bug fix **Gmail (TAN-4543)**

Resolved an issue with authentication via token when connecting to Gmail that blocked the dispatch of emails.

### Release Version 24.16.2

*Release date: 30-April-2024 *#### Improvements **DHL (FFU-2617)** Provisional return label formats can now be configured as either shipping label or DIN A4 format. ** POS (FAC-3102)**

The POST api/posJournals has been updated to store and retrieve a fiscalizationDocument in the POS Journal table.

#### Bug fixes **Settings Center (TAN-4512)** Resolved an issue where a settings view only opened after clicking twice. All settings now correctly open on the first click again. ** Mini detail (PIM-2156)** Mini details of purchase prices are now hidden for users without viewing permissions. ** Invoice (FFU-3389)** Resolved an issue with sending invoice emails with more than one attachment. ** Fast goods receipt (FFU-3180)** Label printing is now possible under all conditions in fast goods receipt. ** PayPal (FAC-2835)** Denied PayPal transactions are now imported with a negated amount if a preceding transaction with the same transaction-id and amount is found in the system. ** Collective debitors (FAC-2028)** Deviating customer numbers are now correctly overwritten if the configuration allows it. They can even be overwritten when they were filled before in documents and contacts. ** Amazon VCS (ECOM-4235)** VCS mechanic will no longer omit product or shipping discounts when the item is sold tax free on Amazon. ** eBay (ECOM-4226)**

Ebay shops with a missing appId or a missing clientId will be de-activated automatically, and a warning will be displayed in systemhealth.

## 24.15 Release and Patch Releases

### Release Version 24.15.0

*Release date: 23-April-2024 *#### Improvements **Printer (PF-2319)** Download links for the NextGen Spooler are now available on the Printer Connections page. ** Kaufland (ECOM-3793)**

Detailed database logging for Kaufland product synchronization errors has been implemented.

#### Bug fixes **Process starter (FFU-3267)** Resolved an issue where the autoversand_plus process starter could not be deactivated when set to run once a day. ** Sales Order API (FFU-2896)** Sales order imports via the salesorderimport API endpoint now correctly include phone and fax numbers from customer addresses. ** eBay payments (FAC-2198)** If there is a mismatch between the tokens saved in an ebay shop and the signature data, needed for ebay payment business account, the signature data will now be corrected automatically. ** Amazon VCS (ECOM-4215)** VCS mechanic will now create invoices for already fetched data even if the associated shop has been disabled. ** Amazon (ECOM-4212)**

When importing sales orders from Amazon, discount items will now have the same tax rate as the product they are associated with.

## 24.14 Release and Patch Releases

### Release Version 24.14.6

*Release date: 16-April-2024 *#### Improvements **Settings Center (TAN-4365)** Back Buttons are now available for settings center views. ** Purchase Price API (PIM-2128)** Add multiple filters to the /api/purchasePrices API endpoint. ** Financial accounting export (FAC-3110)** In case no explicit exchange rate is provided, the Datev exported documents now take the known exchange rate as of the invoice/credit note date. ** DATEV Connect Online (FAC-2813)** Updated the implementation of our DATEV Connect Online solution in order to make use of the latest DATEV API. ** Shopify (ECOM-4028)**

Updated Shopify API from version 2023-04 to version 2024-01.

#### Bug fixes **Device Gateway (PF-2428)** Fixed a performance problem related to the Device Gateway. ** Email accounts (TAN-4461)** The success message language when deleting an email account has been corrected. ** Returns (FFU-3337)** Resolved an issue where saving a return caused an SQL error. ** Transfers (FFU-3327)** Resolved an issue where importing returns via the Transfer module led to a return without any items. ** Purchase order (FFU-3316)** Resolved an undefined method error that occurred when opening a purchase order. ** Warehouse (FFU-2958)** Filtering by article subcategories has been restored in the warehouse management module. ** Sales Order API (FFU-2739)** Creation of SalesOrder did not take over the customer number from the customer master data (contacts table). This has been fixed. Customer number will now be filled based on the data of the customer master data. ** Payment transactions (FAC-1697)** Deleted liabilities no longer appear as open payments in the payment transactions module. ** Amazon VCS (ECOM-4242)** We are pausing the ongoing migration to the new VCS mechanic because we identified certain configurations that can potentially lead to duplicated invoices. ** Amazon (ECOM-4236)** Resolved an issue with the import of Amazon sales orders. ** Shopify (ECOM-4129)**

Logging for all Shopify API communication has been implemented.

## 24.13 Release and Patch Releases

### Patch Version 24.13.5

*Release date: 12-April-2024 *#### Bug fix **Amazon VCS (ECOM-4242)**

We are pausing the ongoing migration to the new VCS mechanic because we identified certain configurations that can potentially lead to duplicated invoices.

### Patch Version 24.13.4

*Release date: 11-April-2024 *#### Bug fix **Transfers (FFU-3327)**

Resolved an issue where importing returns via the Transfer module led to a return without any items.

### Patch Version 24.13.3

*Release date: 10-April-2024 *#### Bug fix **Device Gateway (PF-2428)**

Fixed a performance problem related to the Device Gateway.

### Release Version 24.13.2

*Release date: 09-April-2024 *#### Bug fix **Auto dispatch (FFU-3257)** Resolved an issue that slowed down the auto dispatch, when a lock wasn't released in specific situations in the sales order process. ** Receipt of payment (FAC-2489)** The Paypal transactions can be matched more accurately in case a fee is added to a transaction. ** eBay (ECOM-4213)**

An appropriate message is now displayed if the connection check fails.

## 24.12 Release and Patch Releases

### Patch Version 24.12.5

*Release date: 04-April-2024 *#### Bug fix **File browser (TAN-4477)**

Resolved an issue that prevented the upload of multiple files for a product at the same time.

### Patch Version 24.12.4

*Release date: 04-April-2024 *#### Bug fix **Auto dispatch (FFU-3257)**

Resolved an issue that slowed down the auto dispatch, when a lock wasn't released in specific situations in the sales order process.

### Release Version 24.12.3

*Release date: 02-April-2024 *#### Improvement **User (PF-2320)** Email fields in user edit forms are now editable, preventing lockouts on Auth0 enabled instances for users without an email. ** Fiskaly (FAC-2886)**

Updated the Fiskaly API to the latest version to ensure the functionality of our POS module.

#### Bug fixes **Email (TAN-4390)** Toast messages are now displayed in the user's language. ** Extended order proposal (FFU-2853)** Fixed an issue where manually changed amounts doubled when creating a purchase order from an extended order proposal with multiple executions. ** eBay (ECOM-4175)** Improved handling of Ebay rate-limits. ** Shopware (ECOM-4144)** Special characters in article descriptions (e.g. `XYZ " 12 `) do not show up escaped (e.g. ` XYZ \" 12`) anymore. ** Amazon VCS (ECOM-4035)**

The introduction of the new VCS implementation has deprecated the configuration options for the older version. It's now not possible anymore to configure the old implementation.

## 24.11 Release and Patch Releases

### Patch Version 24.11.6

*Release date: 28-March-2024 *#### Improvement **Fiskaly (FAC-2886)**

Updated the Fiskaly API to the latest version to ensure the functionality of our POS module.

### Patch Version 24.11.5

*Release date: 27-March-2024 *#### Bug fix **Auto dispatch (FFU-3257)**

Resolved an issue that slowed down auto dispatch in specific instances.

### Release Version 24.11.3

*Release date: 26-March-2024 *#### Improvements **Email (TAN-3801)** A new mail log has been introduced that shows all sent emails, their status, and possible solutions for common errors. ** Split shipping (SPS-42)** Added the option to filter by project in the Split shipping (Versand aufsplitten) module. ** Webhooks (PF-2338)**

The endpoints to manage Webhook configuration are now public.

#### Bug fixes **Dunning (FAC-2733)** The email for dunning processes now overrides the project settings email if both are specified. ** Split shipping (FAC-3019)** Taxes are now correctly allocated when there are multiple shipping positions. ** Shipping center (FFU-1451)** Fixed an issue that caused the creation of duplicate invoices in the auto dispatch process. ** Dropshipping (FFU-2150)** Fixed an issue that caused closed dropshipping orders to be processed again. ** Shipping method: Address label (FFU-3173)** Variables now load from correct document in addresslabel shipping method. For document references the variables {AUFTRAG_BELEGNR} and {LIEFERSCHEIN_BELEGNR} can now be used. ** Contacts (TAN-3036)**

Values for federal states can now be saved for contact persons.

## 24.10 release and patch releases

### Release Version 24.10.6

*Release date: 19-March-2024 *#### Improvements **Transfers (FFU-3169)** Additional fields for sales order import have been added. ** Sales order API (FFU-3069)** Project setting "Auto reservation in warehouse" was not obeyed during Sales Order Import via API/ api/ salesOrders/ actions/ import. This has been fixed. ** System health (ECOM-4158)** Introduced the ability to reset System Health messages for Amazon marketplaces. ** eBay (ECOM-4123)**

Shops with invalid authentication tokens will now be disabled and a system health entry will be displayed as a notification.

#### Bug fixes **Product (PIM-2052)** Resolved an issue where CSV product import was truncating data. ** Sales orders (FFU-3103)** Batch releasing sales orders via the sales order overview list didn't work anymore. This has been fixed. ** Sales order (FFU-3197)** Restored buttons that were missing in the positions view of the sales order. ** Dropshipping Warehouse (FFU-2981)** Project filters are now favored over non-project filters when set at the same priority level. ** Production (FFU-2700)** Ensured that the "is-quantity" is now correctly assigned when completing a production through bulk batch processing. ** Amazon (ECOM-4157)** Improved Amazon FBA B2B order import to ensure no orders go missing. ** User interface (PIM-2082)** Reverted changes to the user interface introduced in 24.10.0 that caused pages to not render correctly. ** Liabilities (FAC-2971)** An error occurred when inserting supplier terms into liabilities. As a result, it was not possible to insert contact details into them. This has been fixed. ** Import Templates (TAN-4442)**

Resolved an issue where CSV files could not be imported after they had been uploaded.

## 24.9 Release and Patch Releases

### Patch Version 24.9.1

*Release date: 13-March-2024 *#### Bug fix **Liabilities (FAC-2971)**

An error occurred when inserting supplier terms into liabilities. As a result, it was not possible to insert contact details into them. This has been fixed.

### Release Version 24.9.0

*Release date: 12-March-2024 *#### Bug fixes **Settings Center (TAN-4352)** Fixed multiple minor issues on setting views. ** Email (TAN-4201)** Email accounts connected via IMAP now put sent mails in the respective "Sent" folder of the email provider. ** Financial accounting export (FAC-2979)** The field "Leistungsdatum" is no longer filled with the value "3011-0001" when no delivery note is available. ** Liability (FAC-2971)** The supplier's terms of payment are now fully inserted into the liability. ** Financial accounting export (FAC-2932)** Improved rounding accuracy for the accounting export in case no validation is applied. ** Amazon (ECOM-4142)**

VCS will no longer create credit notes or invoices with shipping discount adding to the price instead of subtracting from it.

## 24.8 Release and Patch Releases

### Release Version 24.8.3

*Release date: 05-March-2024 *#### Improvements **User interface (PF-2008)** The "Pro" badge on apps is now only shown when you are using the "Starter" or "Business" plan of Xentral. ** FinAPI (FAC-2894)** In case of an error, there is now an option to entirely remove the connection and start connecting from scratch. ** Backend (SRE-1967)**

Cloud events are now published to a dedicated queue to improve the performance of all Xentral instances.

#### Bug fixes **Settings Center (TAN-4314)** Tooltips are now available in the settings center. ** Fast goods receipt (FFU-3129)** Fast goods receipt is working again after a bug was introduced in 24.8.0. ** Transfers: Brickfox (FFU-3014)** The company in a delivery address is now correctly transferred to the sales order. ** Sales order (FFU-1594)** Resolved an issue where the filter "only customers with multiple orders" incorrectly showed an empty table. ** Mollie (FAC-2557)** Mollie payments will now be booked with the date of the payment transaction and not the date of the originating order. ** eBay (ECOM-4146)**

Setting an eBay category for a product will no longer invalidate the user token within the settings.

## 24.7 Release and Patch Releases

### Release Version 24.7.5

*Release date: 27-February-2024 *#### New feature **Financial accounting export (FAC-2898)**

Customer data can now be exported from a specific start date. To export all data as before, leave the date fields empty.

#### Improvements **Sales Order API (FFU-2957)** Enhanced the positions list of the SalesOrder VIEW endpoint with additional parameters: id, hasChildren, parent, sort. ** API documentation (FFU-2898)** Updated API documentation to clarify that currency is required for sales order import. ** PDF archive (FAC-2896)**

Invoice and credit note PDF archives will now be generated automatically when the document is approved.

#### Bug fixes **NextGen user interface (XIN-903)** Resolved an issue where Analytics tiles on the Launchpad were shown to non-admin users and displayed error messages because those users do not have the permission to see data for these tiles. The tiles are now hidden from non-admin users. ** Xentral Returns Portal (PF-2266)** The Xentral Returns portal module has been missing on several instances after an update due to an issue with license properties. This has been fixed. ** User interface (PIM-2021)** It is now again possible to interact with the header and sidebar after opening a modal. Non-admin users will see their navigation again. ** Calendar (PIM-2015)** Calendar entries are now only displayed once if a user is in calendar groups where some entries are identical to other calendars. ** Ticket System (TAN-4288)** Resolved an issue causing emails without a content-type header to be imported without content. ** Business letter templates (FFU-3010)** Corrected collective invoices to no longer display unrelated tracking numbers. ** Delivery note (FFU-2899)** The delivery note filter "not retrieved from stock" was not showing results. This has been fixed. ** Mobile Inventory App (FFU-2819)** Some warehouse-level aggregate shelf statistics on the Mobile Inventory Reports overview page were partly incorrect. This has been fixed. ** Production (FFU-2474)** In some cases the bill of materials were not expanded (exploded) correctly. This has been fixed. ** Best before date (FFU-1436)** Batch/BBD entries were displayed multiple times in the batch/BBD overview when "group by batch" was enabled. This has been fixed. ** Commission agent (FAC-2907)** Resolved an issue that caused a 500 error when creating a commission agent. ** Amazon (ECOM-4155)** Amazon rate limits on new shipping address endpoint will no longer block sales order import. ** eBay (ECOM-4152)** Resolved an issue where automatic stock synchronization for eBay was not working as intended. ** Magento 2 (ECOM-4095)** Magento 2 sales order import can now fetch more than one order per iteration. ** Amazon (ECOM-3927)** Amazon order import carries over VAT ID correctly for B2B FBM orders. ** Amazon (ECOM-3907)** Improved reliability in displaying buyer company names by using a more suitable endpoint for Amazon Shipping Addresses. ** Amazon Seller App (ECOM-3860)** The Amazon Seller App no longer displays deleted products. ** POS (CCI-2000)**

Fixed an issue where the POS module's user interface did not display correctly when operating in a Docker environment.

## 24.6 Release and Patch Releases

### Patch Version 24.6.4

*Release date: 23-February-2024 *#### Bug fixes **Business Letter Template (FFU-3010)** Collective invoices no longer display unrelated tracking numbers. ** eBay (ECOM-4152)**

Resolved an issue where automatic stock synchronization for eBay was not working as intended.

### Release Version 24.6.2

*Release date: 20-February-2024 *#### Improvements **Settings center (TAN-4203)** Users with administration rights are now able to manage permissions for all settings pages and can control which user has access to which view in the settings center. ** Products API (PIM-1978)** Freefield names are now properly shown in the GET /api/products/ endpoint. ** NextGen UI (PIM-1905)** A loading indicator at the top of the module is now visible on all modules during loading in the NextGen. ** DATEV (FAC-2597)**

The Datev XML Export now allows to export both transaction number and internet number in the orderId XML field.

#### Bug fixes **Sendcloud (FFU-3005)** Resolved an issue with downloading the customs declaration form for Sendcloud shipments after successful label creation. ** Process starter (FFU-2901)** Resolved PDF-related errors in the autoversand_plus process. ** UPS OAuth (FFU-2712)** Added missing reference information to UPS OAuth shipping labels. ** Sales order (FFU-2485)** Sales order numbers were sometimes not consecutive, but had gaps. This has been fixed. ** Database migration (SRE-1973)** Database migrations run again after update. ** Product export (ECOM-4088)** Products with apostrophes in their product name will now appear in the logfile in case of an error during product export. ** Stock numbers (ECOM-3948)**

Stock updates due to order cancellations of JIT (Just in time) bill of materials are now correctly transmitted to sales channels.

## 24.5 Release and Patch Releases

### Patch Version 24.5.4

*Release date: 13-February-2024 *#### Bug fix **Sendcloud (FFU-3005)**

Resolved an issue with downloading the customs declaration form for Sendcloud shipments after successful label creation.

### Release Version 24.5.3

*Release date: 13-February-2024 *#### New feature **Shipping method: Address label (FFU-2872)**

The addresslabel shipping method now allows using variables such as {AUFTRAG_BELEGNR} or {LIEFERSCHEIN_BELEGNR} to reference the related document numbers on the label or in barcodes.

#### Improvements **NavBar (TAN-4165)** Links to three new shop connections (Big Commerce, Shopware 5 + 6) are now available for Early Access users. ** Email (TAN-3990)** When sending documents, or writing emails from the E-Mail Archive module or from the CRM tab in the Contacts module, users can only select email addresses to send from, from existing accounts that are shared with them or everyone. ** Report / Template Export / Import (SPS-43)** Quotes added as default masking. ** Printer (PF-2188)** Users can now provide feedback on the printer wizard directly within the printer connections page. ** Commission run (FFU-2858)** Added a reprint button to overview tables in the commission run. ** Sendcloud (FFU-2662)**

Implemented an 'Exclude JIT components' checkbox for the Sendcloud shipping method.

#### Bug fixes **Settings center (TAN-4290)** Shop Connector and Printer views can be accessed again in the settings center. ** Email (TAN-4254)** Resolved compatibility issues with certain email providers. ** NextGen Settings (TAN-4166)** Added further settings for the follow-up module. ** Report (SPS-24)** Resolved an issue with sending reports via SFTP-** Import template (SPS-18)** Enabled importing purchase prices with both comma and dot as price delimiters. ** Commission (SPS-13)** Adjustments made to prevent the use of expired purchase prices in 'provisionenartikelvertreter'. ** Product (PIM-1958)** Resolved an issue in bulk processing where data from the first line was not copied correctly across products. ** Delivery note (FFU-2949)** There was an issue with creating the PDF of delivery notes when a property was missing in the shipping method attached to the delivery note. Previewing and creating PDFs now works again correctly. ** Business letter template (FFU-2885)** Corrected the DHL 3.0 value in the {VERSAND} variable in the business letter templates. ** Sales Order Import API (FFU-2810)** The Sales Order Import API had issues with applying the correct foreign currency on the document level (currency on the position level was applied correctly). This has been fixed so that the currency on the document level is also set correctly. ** Production (FFU-2879)** Resolved overproduction calculation. ** Extended Order Proposal / Production (FFU-2773)** Issue of missing part-items on batch-processing of productions resolved. ** Sending Documents (FFU-2563)** Tracking links with special parameter strings are now displayed correctly. ** Cost center (FAC-2857)** Cost centers with more than 10 characters can now be used in the sales order, delivery note, offer, and respective accounting exports. ** Financial accounting export (FAC-2838)** When exporting to CSV and using a separate financial account, discounts were creating negative values which caused issues with DATEV. Incorrect negative values are now correctly displayed as positive in the CSV financial export. ** Taxdoo (FAC-2751)** Improved payment date validation in Taxdoo exports. ** Mollie (FAC-2521)** Mollie refunds, based on a Shopify order, can be triggered again. ** Category tree (ECOM-4102)** Category tree export for Shopware 5, Shopware 6, Spryker, Presta and Magento 2 is working again. ** Shopify (ECOM-4068)** In order to provide visibility on missing scopes/permissions for accessing the Shopify API, all Shopify API errors are now displayed in the logfile. ** Shopware (ECOM-3993)** For Shopware 6.5, uploading invoices to Shopware after the shipment has been sent did not work. This is fixed. ** Process starter (CCI-1972)**

Optimized performance of the "zahlungseingang" process starter: the amount of documents that are matched against incoming payments can now be limited for each bank or payment account.

## 24.3 Release and Patch Releases

### Patch Version 24.3.4

*Release date: 05-February-2024 *#### Improvement **Email (TAN-4280)**

Added a new message if an email can't be sent due to an incorrect email configuration. This message includes a note on how to configure your email correctly.

### Patch Version 24.3.3

*Release date: 02-February-2024 *#### Bug fix **Delivery note (FFU-2949)**

There was an issue with creating the PDF of delivery notes when a property was missing in the shipping method attached to the delivery note. Previewing and creating PDFs now works again correctly.

### Release Version 24.3.2

*Release date: 30-January-2024 *#### Improvement **User (PF-2137)**

Inviting a new user without linking them to an address (contact), will give them a new contact (adresse) with the role "Employee".

#### Bug fixes **Subscription (SPS-29)** Resolved discrepancy between pre-calculation and actual creation in weekly subscriptions. ** Auth0 (PF-2075)** Enhanced the speed of web requests of users using Auth0, to improve overall performance of the system. ** Mobile Inventory App (FFU-2870)** Previously, the PDF report for a counting list could only be generated for committed inventory runs. However, it is now possible to generate the report for uncommitted inventory runs as well. ** Transfers (FFU-2642)** The transfer module had issues applying the prefix to outgoing transfers. This has been fixed so that that prefix is considered in the filename on the outgoing transfer. ** Swiss QR (FAC-2836)** Swiss QR code will now only be printed on the invoice when the payment method type is Invoice. ** PayPal (FAC-2830)**

Paypal fees will now be booked automatically if the relevant checkbox is set in the business account.

#### Removal **Amazon Vendor DF (ECOM-4031)**

Functionality for Amazon VendorDF has been removed.

## 24.2 Release and Patch Releases

### Patch Version 24.2.8

*Release date: 25-January-2024 *#### Bug fix **Import central (SPS-34)**

Resolved issues with importing CSV files that contain quotation marks.

### Release Version 24.2.7

*Release date: 23-January-2024 *#### Improvements **GLS API (FFU-2812)**

GLS shipping labels can now also be printed in stage 1 of the logistics process if the respective check box is selected.

#### Bug fixes **Email (TAN-3707)** A default queue can now be assigned to an email address. ** Shipping method: Amazon Prime (FFU-2873)** Amazon Prime shipping labels can be printed again. ** DHL (FFU-1554)** The tracking link was missing in emails when using the {VERSAND} variable in the business letter templates for the shipping method DHL. This has been fixed. ** Swiss QR (FAC-2808)** Swiss IBANs which contain an institute id (QR IBAN), are no longer allowed for the modes NON and SCOR. ** Payment transactions (FAC-2165)** Invalid SEPA XML files were created when the name of the recipient contained more than 35 characters. A length check has been implemented to ensure that the XML files are valid. ** Shopify (ECOM-4045)** Resolved an issue with importing sales orders through third party apps in Shopify. ** Shopimporter (ECOM-4037)**

Resolves an issue that might occur when importing sales orders from the intermediate table.

## 24.1 Release and Patch Releases

### Patch Version 24.1.8

*Release date: 19-January-2024 *#### Bug fix **Shopify (ECOM-4045)**

Resolved an issue with importing sales orders through third party apps in Shopify.

### Patch Version 24.1.7

*Release date: 18-January-2024 *#### Bug fixes **Shopify POS (ECOM-4044)** Sales orders from Shopify POS are fetched correctly again. ** Mobile Inventory App (FFU-2869)** The counting list accurately displays all registered storage locations during an inventory run, irrespective of the status or contents of the shelves. ** Mobile Inventory App (FFU-2868)**

Issues in the inventory run commitment process, stemming from specific combinations of batch and best before dates, have been addressed and resolved.

### Patch Version 24.1.6

*Release date: 17-January-2024 *#### Bug fix **Shopify (ECOM-4039)**

The Shopify sales order import is now working again as intended.

### Patch Version 24.1.5

*Release date: 16-January-2024 *#### Bug fix **Statistics (FFU-2856)**

Resolved an issue with filtering by project in the Statistics module.

### Release Version 24.1.4

*Release date: 16-January-2024 *#### Improvements **Emails (TAN-3798)** Added a new feature to send emails asynchronously in the background. ** User (PF-1585)** Improved the legacy two-factor authentication with one-time password. ** Financial accounting export (FAC-2770)** The delivery date (Leistungsdatum) field is now included in both CSV and XML outputs of the financial accounting export for invoices and liabilities. Specifically for liabilities, the Eingangsdatum or entry date will be considered as delivery date. ** Financial accounting export (FAC-2743)**

Adjusted DATEV export to include liability attachments with the keyword 'Anhang' (Invoice Attachment); documents without this keyword will be excluded from the export.

#### Bug fixes **eBay (SRE-1880)** Improved speed of sending image files to the eBay module. ** Report (SRE-1868)** Resolved cache issue in API export. ** Item tree (PIM-1870)** Resolved the issue of previously soft-deleted product categories reappearing in the item tree. ** Datev Connect online (PIM-1861)** Liabilities which appear in the error message of Datev Connect have a correct URL to open them immediately. ** Product (PIM-1853)** Resolved issues in the product list view where customers encountered empty pages or incorrect product counts. ** Printer (PF-2066)** The download button, when printing to a download printer, is now working correctly, ** Delivery note (FFU-2843)** All entries in the delivery note overview table disappeared when clicking the menu column. This has been fixed. ** Commission agent (FAC-2818)** Resolved crashing of the application when calculating commissions for credit-notes. ** DATEV (FAC-2817)** In DATEV Company Online and Connect Online, the Liability PDF export will now consider documents with the keyword "belege", if there are no available documents with keyword "anhang". ** Receipt of payment (FAC-2744)** Over/double payments for paid orders will no longer be automatically assigned to the respective order/invoice. ** PayPal (FAC-2723)** PayPal fees will now be booked automatically if the relevant checkbox is set in the business account. ** Credit notes (FAC-2719)** Credit notes which are assigned to already paid invoices will no longer be automatically marked as completed. ** Document tables (FAC-2700)** Resolved an issue where actions in the mini-detail are executed for the wrong document when multiple documents are opened. ** Invoice (FAC-2649)** Skonto / Discount will no longer be displayed twice in the invoice protocol. ** Shopimporter (ECOM-4022)** Resolved a validation error that caused problems with the import of sales orders. ** Update process (CCI-1961)**

Resolved an issue where users were unable to login after updating from an older Xentral version (e.g., 21.1).

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