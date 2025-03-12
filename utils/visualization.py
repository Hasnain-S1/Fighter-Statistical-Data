import plotly.graph_objects as go
import plotly.express as px

def create_spider_chart(fighter1_metrics, fighter2_metrics, fighter1_name, fighter2_name):
    categories = list(fighter1_metrics.keys())

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=list(fighter1_metrics.values()),
        theta=categories,
        fill='toself',
        name=fighter1_name,
        line_color='#ff4b4b'
    ))

    fig.add_trace(go.Scatterpolar(
        r=list(fighter2_metrics.values()),
        theta=categories,
        fill='toself',
        name=fighter2_name,
        line_color='#00ff88'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    
    return fig

def create_stats_bar_chart(stats, title):
    fig = px.bar(
        x=list(stats.keys()),
        y=list(stats.values()),
        title=title
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False
    )
    
    return fig
