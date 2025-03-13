import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processor import get_fighter_stats
from utils.visualization import create_stats_bar_chart

def weight_class_breakdown_page(df):
    st.title("🏆 Weight Class Breakdown")
    st.write("View statistics and rankings for each UFC weight class.")

    # Select weight class
    weight_classes = sorted([wc for wc in df['weight_class'].unique() if wc is not None])
    weight_class = st.selectbox("Select Weight Class", weight_classes)

    # Filter the dataset by selected weight class
    filtered_df = df[df['weight_class'] == weight_class]

    # Display the fighters in the selected weight class
    fighters = sorted(filtered_df['name'].unique())
    st.write(f"### Fighters in the {weight_class} division")
    st.write(f"Total Fighters: {len(fighters)}")
    st.write(fighters)

    # Display key metrics for each fighter
    metrics_columns = ['name', 'significant_strikes_landed_per_minute', 'significant_striking_accuracy',
                       'significant_strikes_absorbed_per_minute', 'significant_strike_defence',
                       'average_takedowns_landed_per_15_minutes', 'takedown_accuracy', 'takedown_defense',
                       'average_submissions_attempted_per_15_minutes', 'reach_to_height']

    # Extract relevant metrics
    metrics_df = filtered_df[metrics_columns]
    
    # Display a table with key metrics
    st.write(f"### Key Metrics for Fighters in {weight_class}")
    st.dataframe(metrics_df)

    # You can also create a bar chart for each of these metrics
    st.markdown("### Key Metric Comparison")
    
    # Select a metric for comparison
    metric_to_plot = st.selectbox("Select Metric for Comparison", metrics_columns[1:], index=1)

    # Create a bar chart comparing the selected metric for all fighters
    fig = px.bar(
        metrics_df, 
        x='name', 
        y=metric_to_plot, 
        title=f"{metric_to_plot} for Fighters in {weight_class}",
        labels={'name': 'Fighter', metric_to_plot: metric_to_plot.replace('_', ' ').title()},
        color='name',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig, use_container_width=True)

    # Additional insights or comparisons can be added here
    st.markdown("### Insights")
    st.write("Use this breakdown to compare fighters within the same weight class.")
    st.write("You can use the charts to spot trends and see how fighters stack up against each other.")
