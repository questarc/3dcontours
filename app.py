import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="3D Contour Plot", layout="wide")

def main():
    st.title("3D Contour Plot App")
    st.markdown("This app generates an interactive 3D contour plot using Plotly. It visualizes a sample surface function with contour lines projected onto the surface.")

    # Sidebar for user inputs
    st.sidebar.header("Plot Parameters")
    num_points = st.sidebar.slider("Number of grid points", min_value=10, max_value=50, value=30)
    amplitude = st.sidebar.slider("Amplitude of the function", min_value=0.5, max_value=3.0, value=1.0)

    # Generate sample data
    x = np.linspace(-5, 5, num_points)
    y = np.linspace(-5, 5, num_points)
    X, Y = np.meshgrid(x, y)
    Z = amplitude * np.sin(np.sqrt(X**2 + Y**2))

    # Create the 3D surface plot with contours
    fig = go.Figure(data=go.Surface(
        z=Z,
        x=X,
        y=Y,
        contours=dict(
            z=dict(
                show=True,
                usecolormap=True,
                highlightcolor="limegreen",
                project_z=True
            )
        ),
        colorscale='Viridis'
    ))

    # Update layout for better visualization
    fig.update_layout(
        title="Interactive 3D Contour Surface",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z"
        ),
        autosize=False,
        width=800,
        height=600,
        margin=dict(l=0, r=0, b=0, t=50)
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)

    
if __name__ == "__main__":
    main()
