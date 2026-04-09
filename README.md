# streamlit-final-project

# MarketMetrics: Campaign Performance Dashboard

## Giana Gentile 

## App Description 
The Marketing Campaign Performance Analyzer is a web application designed to help users analyze and track the performance of their marketing campaigns using key metrics and interactive visualizations. Users can input their own campaign data, explore trends, and evaluate campaign effectiveness based on Click-Through Rate (CTR) and Conversion Rate calculations. The app provides real-time feedback and input validation to ensure accurate, meaningful results.

## Intended Users 
This app is ultimaelty intended for marketing students, analyics students, and business who want to understand and evaluate the performace of marketing campagins. It helps the intended users to evaluate the campaign performace, strengthen data interpertation skills and compare overall effectiveness of the campagin. 

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

## Final Features 
1. Data Input
   - Users can manually enter their campaign data i.e. impressions, clicks, conversion, name, and channel.

2. Automatic Calculation and Feedback
   - MarketMetrics automatically and seamlessly calculates Click-Through-Rate and Conversion rate based on user inputs. Futhermore, users recieve an immediate evaluation/feedback of their campagins metrics.
     
3. Input Validation
   - The app is programed to prevent unrealistic data entries and dispays error message if done so. (ex: more clicks than impressions)
     
4. Charts and Visualization
   - The impression, clicks, and conversion data are displayed in interactive/clean graphs and charts.
     
5. Custom Data Set Upload Feature
   - Users can optionally upload their own dataset to analyze bigger and more complex data.
     
6. Multi-Campaign Comparison
   - Users can compare multiple campagins side by side to determine most effective attributes/strategies.

## Deployed App 
https://app-final-project-cbktvdymddwuvpv3utkkz3.streamlit.app

## How to Use the App 
1. Click the link to launch app in web-browser
2. Enter Campaign Data - enter the name of campagin, channel it is on, number of clicks, impressions, and conversions in the provided fields.
3. View Caculated Data - after data is provided, the app will automatically calculate and display the Click-Through-Rates and Conversion Rates
4. Review data provided buy understanding the calculations and what they mean for your campagin
5. Use Visualizations - use the chart data to get a better understanding of data and interact with charts/graphs
6. Upload Dataset (Optional but Suggested)- Use the upload feature to import a custom CSV file with columns 'Campaign', 'Channel', 'Impression', 'Clicks', 'Conversions' for more advanced data analysis
7. Compare Compagins (Optional) - The app allows you to add multiple campagins to compare their performance metrics side by side instantly.
8. For CSV Uploads: the app allows you to download the calcualted results as a new CSV. 
