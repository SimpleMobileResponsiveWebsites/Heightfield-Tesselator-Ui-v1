import streamlit as st
import json
from pathlib import Path

# Streamlit app for configuring HeightfieldTesselator settings
def main():
    st.title("HeightfieldTesselator Configuration")

    # Sidebar for loading/saving configurations
    st.sidebar.header("Manage Configurations")
    
    # Load configuration file
    config_file = st.sidebar.file_uploader("Load Configuration", type=["json"])
    if config_file is not None:
        config = json.load(config_file)
        st.sidebar.success("Configuration loaded successfully!")
    else:
        # Default configuration
        config = {
            "heightfield_image": "",
            "focal_point": [0.0, 0.0],
            "horizontal_scale": 1.0,
            "vertical_scale": 255.0,
            "polygon_count": 10000,
            "visibility_radius": None,
            "max_triangles": None,
            "map_details": {
                "terrain_type": "plain",
                "water_level": 0.0,
                "vegetation_density": 0.5
            }
        }

    # Editable inputs for configuration
    st.header("Terrain Configuration")

    config["heightfield_image"] = st.text_input(
        "Heightfield Image Path",
        value=config.get("heightfield_image", "")
    )

    focal_point = config.get("focal_point", [0.0, 0.0])
    config["focal_point"] = [
        st.number_input("Focal Point X", value=float(focal_point[0]), step=1.0),
        st.number_input("Focal Point Y", value=float(focal_point[1]), step=1.0)
    ]

    config["horizontal_scale"] = st.number_input(
        "Horizontal Scale",
        value=config.get("horizontal_scale", 1.0),
        step=0.1
    )

    config["vertical_scale"] = st.number_input(
        "Vertical Scale",
        value=config.get("vertical_scale", 255.0),
        step=1.0
    )

    config["polygon_count"] = st.number_input(
        "Polygon Count",
        value=config.get("polygon_count", 10000),
        step=100
    )

    config["visibility_radius"] = st.number_input(
        "Visibility Radius (Optional)",
        value=config.get("visibility_radius", 0.0) or 0.0,
        step=1.0
    )

    config["max_triangles"] = st.number_input(
        "Max Triangles (Optional)",
        value=config.get("max_triangles", 0) or 0,
        step=100
    )

    # Editable inputs for map-specific details
    st.header("Map Design Details")

    config["map_details"]["terrain_type"] = st.selectbox(
        "Terrain Type",
        options=["plain", "mountain", "desert", "forest"],
        index=["plain", "mountain", "desert", "forest"].index(config["map_details"].get("terrain_type", "plain"))
    )

    config["map_details"]["water_level"] = st.slider(
        "Water Level",
        min_value=0.0,
        max_value=1.0,
        value=config["map_details"].get("water_level", 0.0),
        step=0.01
    )

    config["map_details"]["vegetation_density"] = st.slider(
        "Vegetation Density",
        min_value=0.0,
        max_value=1.0,
        value=config["map_details"].get("vegetation_density", 0.5),
        step=0.01
    )

    # Display the current configuration
    st.subheader("Current Configuration")
    st.json(config)

    # Save configuration
    if st.button("Save Configuration"):
        save_path = st.text_input("Enter file name to save (e.g., config.json)")
        if save_path:
            with open(save_path, "w") as f:
                json.dump(config, f, indent=4)
            st.success(f"Configuration saved to {save_path}")
        else:
            st.error("Please provide a file name to save.")

    # Export configuration
    st.download_button(
        label="Export Configuration as JSON",
        data=json.dumps(config, indent=4),
        file_name="heightfield_config.json",
        mime="application/json"
    )

    # Placeholder for potential preview functionality (requires Panda3D rendering environment)
    st.info("Note: Preview rendering not available in this app.")

if __name__ == "__main__":
    main()
