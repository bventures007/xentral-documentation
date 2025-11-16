With xentral you can automatically transfer your sales to Taxdoo. Taxdoo monitors on a daily basis whether delivery thresholds abroad have been exceeded. Exchange rates and different tax rates in the respective country are automatically taken into account and you can manage the sales centrally and transfer them to your tax office.

Schritte

1. Step 1
1. Step2 asfsdfdsa
1. Schritt 3

> **Warnung**
>
> **Warning**
>
> Text von der Warning

> **Anmerkung**
>
> Make sure that the data is complete. Otherwise the first transfer may fail!

> **Anmerkung**
>
> The "Seller data" is so to speak your business and designates you as the "owner of the store" The business on whose behalf data is transferred to Taxdoo.

3. Choose the start date from when you want to export sales to Taxdoo.

## Features

After you have connected xentral to Taxdoo, the following options are available to you:

- xentral automatically transfers completed sales and credits based on orders and invoices
- Transfer via the Taxdoo API possible until the beginning of the following month - here Taxdoo closes the current month and you should have transferred all receipts
- Log of transferred sales and credit notes/cancellations
- Projects (sales channels) can be included or excluded
- Start date for transfers to Taxdoo is adjustable

> **Anmerkung**
>
> **Note**
>
> This is a note!

### Steps

- Click in the App Center > Taxdoo > Settings. Here you will find the settings to connect your xentral with Taxdoo. (See for example data the image)
- Number 2

## Connect Taxdoo with xentral

### Steps

- Click in the App Center > Taxdoo > Settings. Here you will find the settings to connect your xentral with Taxdoo. (See for example data the image)

2. Fill in the access data

- Taxdoo Token. You can get this from the customer area in your Taxdoo backend via Settings > API.
- Enter your "seller data". These are mandatory fields in xentral, which Taxdoo needs to accept a transfer.
  The following has to be entered:

  Seller name* → Your company name e.g. "Musterfirma GmbH "

  Seller street → Street + HNr. of the company

  Seller zip code* → Postal code of the company

  addressSeller city → City of the company

  addressSeller federal state* → Federal state of the company address e.g. "Bavaria "

  Seller country (ISO-2)* → ISO country code e.g. "DE" for Germany

> **Anmerkung**
>
> Make sure that the data is complete. Otherwise the first transfer may fail!

> **Anmerkung**
>
> The "Seller data" is so to speak your business and designates you as the "owner of the store" The business on whose behalf data is transferred to Taxdoo.

3. Choose the start date from when you want to export sales to Taxdoo.

**Note**

Best practice

Start with the current month to import or for the month overlap with the last day of the previous month e.g.: 30.03. or 1.4. to pick up April.

**Info**

Without this date there is no limit in the export, i.e. if the receipts are further back than the last month, please set a start date. Once the transfer is ongoing, it will always be exported regularly by status until Taxdoo closes the batch on the 7th of the following month. This is then only a problem if receipts flow into an ERP subsequently or retroactively.

4. The following settings are special settings for special cases that you probably don't need in the first step.

This information will help you to check whether the settings are required for your use case:

Exclude the following projects.

Projects can be excluded from export to Taxdoo. The function must be activated and the project to be excluded must also be entered in the list below via "new entry".

(Logging. For xentral internal for error detection in data transfer)

Sandbox. Needed for a test with the Taxdoo sandbox (needed for testing, test instance, preview etc., it is possible to get a test version of Taxdoo)

Exclude Amainvoice receipts. The Amazon receipts will not be sent to Taxdoo in this case to avoid duplicate transfers from two systems. The receipts that are created via Amainvoice will be excluded.

## Transferring the sales

You can transfer the following sales and receipts to Taxdoo via xentral:

- Sales (orders with invoice)
- Credit notes / cancellations

### Sales

xentral transfers completed sales with invoice document. This means orders with status "completed" that have been forwarded to an invoice. The invoice must have the status "sent".

Sales without positions or with order value 0,00 Euro will not be transferred.

### Credit notes / cancellations

xentral transfers credit notes / cancellation invoices that have been forwarded from an invoice. Make sure that your credit note / cancellation invoice has the status "released" or "sent". The corresponding invoice must have at least one invoice number and must not be in draft mode.

So that your credit note is transferred you must ensure the following:

- You have entered a date in the "completed on" field in the credit memo.
- OR: you use the incoming payment and have linked a money transfer to the credit note and have a total cleared balance.Example: a customer pays you 100 EUR, cancels 25 EUR and you pay your customer back the 25 EUR. In this case you have continued the invoice as a credit note and linked the 25 EUR refund to your credit note. The total balance is therefore balanced (and ACTUAL >= TARGET).

> **Anmerkung**
>
> Info
>
> Orders with invoice status "cancelled" are also transferred. I.e. if you continue an invoice to a credit note or cancellation invoice, the turnover (order) is reported to Taxdoo of course. The credit note / cancellation invoice is also transferred.

### Activate process starter for the transfer

In order to transfer your sales to Taxdoo automatically, activate the process starter in xentral via the button "Activate process starter" (Alternatively you can click on the link in the status message, it has the same function).

The transfer will now start automatically in the time frame set in your process starter (once per day is sufficient).

![2521006091.png](https://help.xentral.com/hc/article_attachments/8795387976092)

> **Anmerkung**
>
> Due to a limitation on the part of Taxdoo, a maximum of 100 orders per minute can be transferred. Please note that data delivered to Taxdoo via API is visible in the Taxdoo dashboard after 24 hours at the earliest (i.e. the timing of the process starter on the xentral side has no influence on this. Once or twice a day is sufficient).

> **Warnung**
>
> If the process starter does not transfer or you want to check the parameters, you can do this directly in the "Process starter" module. In the list you can also find the recommended default parameters that you should use.

## Functions in xentral - Tabs

### Transfer

The Transfer tab displays the orders that have already been transferred to Taxdoo.

In the info message in this tab you can see how many orders are currently ready to be transferred.

> **Anmerkung**
>
> Invoices created without an order in xentral are not taken into account. The central document is the completed order, from which the invoice usually follows. If the transfer does not work automatically, you can mark the invoice as "sent". Then the orders will be queued for transmission.

### Failed

The Failed tab displays the failed orders that have not been transferred to Taxdoo. Here you can also see the reasons why a transfer failed.

If one of your sales has not been transferred to Taxdoo because Taxdoo has rejected an order, it is possible to retrigger it in xentral.

However, if this sale has been transferred and is incorrect, a new transfer from xentral is not possible, the transaction is rejected by Taxdoo. The reason for this is a duplicate recognition on the part of Taxdoo.

## FAQ I send my orders from another time zone to Taxdoo

Note that there may be a time zone shift and that the German time zone may be displayed differently for your orders in xentral. Taxdoo always interprets the data in the time zone Coordinated universal time (UTC+0). Timezone Berlin would be UTC+2.

I.e. for the transfer. to Taxdoo takes xentral not by date, but the possible sales.

For the date representation in Taxdoo, however, a day shift can result.

![grey_arrow_down.png](https://help.xentral.com/hc/article_attachments/8795387991196)

I send my orders from another time zone to Taxdoo

Note that there may be a time zone shift and that the German time zone may be displayed differently for your orders in xentral. Taxdoo always interprets the data in the time zone Coordinated universal time (UTC+0). Timezone Berlin would be UTC+2.

I.e. for the transfer. to Taxdoo takes xentral not by date, but the possible sales.

For the date representation in Taxdoo, however, a day shift can result.