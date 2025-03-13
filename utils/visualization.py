import plotly.graph_objects as go
import plotly.express as px

def create_spider_chart(fighter1_metrics, fighter2_metrics, fighter1_name, fighter2_name):
    categories = list(fighter1_metrics.keys())

    fig = go.Figure()
    
    # Fighter 1 trace
    fig.add_trace(go.Scatterpolar(
        r=list(fighter1_metrics.values()),
        theta=categories,
        fill='toself',
        name=fighter1_name,
        line=dict(color='#1f77b4', width=3),  # Blue color with thicker line
        opacity=0.8
    ))

    # Fighter 2 trace
    fig.add_trace(go.Scatterpolar(
        r=list(fighter2_metrics.values()),
        theta=categories,
        fill='toself',
        name=fighter2_name,
        line=dict(color='#ff7f0e', width=3),  # Orange color with thicker line
        opacity=0.8
    ))

    # Layout improvements
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True, 
                range=[0, 100],
                gridcolor='gray',  # Improved visibility
                gridwidth=0.5
            )
        ),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=14)  # Bigger font for better readability
    )
    
    return fig

def create_stats_bar_chart(stats, title):
    fig = px.bar(
        x=list(stats.keys()),
        y=list(stats.values()),
        title=title,
        color=list(stats.keys()),  # Adds color differentiation
        color_discrete_sequence=px.colors.qualitative.Pastel  # Soft, readable colors
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=14),
        showlegend=False
    )
    
    return fig
