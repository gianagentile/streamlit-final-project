# streamlit-final-project

# MarketMetrics: Campaign Performance Dashboard

## Giana Gentile 

## App Description 
My app's intended use is to help users analyze and track the performance of marketing campaign. This is done by utilizing key metrics and interactive visualizations. In the app, users will be able to explore/examine campgain data, identify trends, and determine the effectiveness of the campgain based on click through rates (CTR) and conversion rates. 

## Intended Users 
This app is ultimaelty intended for marketing students, analyics students, and business who want to understand and evaluate the performace of marketing campagins. 

## Added Features  
- Feature 1: Users can input campaign data (impressions, clicks, conversions)
- Feature 2: Automatic calculation of key metrics (CTR and Conversion Rate)
- Feature 3: Real-time feedback and performance evaluation based on input
- Feature 4: Input validation to prevent unrealistic values

## Planned Features 
- Feature 1: Add charts and visualizations - turning the users impressions and clicks into charts/graphs 
- Feature 2: Allow users to upload their own dataset - allows analyzation of larger and/or custom data 
- Feature 3: Add comparisons between multiple campaigns - can compare multiple campagins simultaneously
- Feature 4: Improve  design and layout

## Challenges 
1. Determining how users would imput the data
   - At first I was planning on using sample data stored in the app but realized that it not interactive or helpful to the user. So instead I wanted the user to enter their own campagin data so it is more interactive and accurate for them. This made me implment streamlit widgets to get here.

2. Validating User Input
   - At first when i was testing my code, users could enter more clicks than impressions which wouldn't make sense. I had to check for these cases and provide an error message in those situations
     
3. Caculations
   - Since the app automatically cacluates CTR and conversion rates based on the inputs I had to figure out the caculations and how to apply them within the code to run smootly and correctly. 
