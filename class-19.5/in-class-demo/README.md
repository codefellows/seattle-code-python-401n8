# Class 19.5 Demo

A Python serverless function deployed to Vercel that takes a news topic in the query string and responds with
the URL of the top AP News search result, and a 4 sentence ChatGPT summary of the article as plaintext.

Deployed at:

- https://class-19-demo.vercel.app/

## Usage

```bash
$ curl "https://class-19-demo.vercel.app/api/news?topic=cars"
```

returns

```text
https://apnews.com/article/used-cars-shopping-prices-01220b1c2cb3c286c146bfed7180a34c

The used vehicle market has been challenging in recent years with high prices and low inventory, but prices have dropped slightly from last year's high, with Edmunds reporting an average transaction price of $28,935 for used vehicles in Q3. Experts at Edmunds suggest that shoppers broaden their search beyond local dealerships, consider higher mileage or older models, and ensure a good vehicle history for the best deals. Prospective buyers are advised to get preapproved for a loan and compare interest rates to lower monthly payments, and they might benefit from trading in their current vehicle due to high used car prices. Certified pre-owned vehicles also present a good option, offering benefits like extended warranties and potentially qualifying for new car interest rates, though the 2023 and 2024 used-car market may still require shoppers to make compromises to find the right deal.
```

