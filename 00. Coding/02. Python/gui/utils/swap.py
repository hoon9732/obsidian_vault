# Swaps Color Palette for themes/.qss files

import re

def swap_rgb_values(rgb_match):
    # Extract the RGB values from the match
    r, g, b = map(int, rgb_match.group(1).split(','))
    
    # Check if a > c > b (r > b > g)
    if r > b > g:
        return f"rgb({r}, {b}, {g})"
    elif g > r > b:
        return f"rgb({g}, {r}, {b})"
    elif g > b > r:
        return f"rgb({g}, {b}, {r})"
    elif b > r > g:
        return f"rgb({b}, {r}, {g})"
    elif b > g > r:
        return f"rgb({b}, {g}, {r})"
    else:
        return rgb_match.group(0)

def swap_rgba_values(rgba_match):
    # Extract the RGBA values from the match
    r, g, b, a = map(int, rgba_match.group(1).split(','))
    
    # Check if a > c > b (r > b > g)
    if r > b > g:
        return f"rgba({r}, {b}, {g}, {a})"
    elif g > r > b:
        return f"rgba({g}, {r}, {b}, {a})"
    elif g > b > r:
        return f"rgba({g}, {b}, {r}, {a})"
    elif b > r > g:
        return f"rgba({b}, {r}, {g}, {a})"
    elif b > g > r:
        return f"rgba({b}, {g}, {r}, {a})"
    else:
        return rgba_match.group(0)

def swap_hex_values(hex_match):
    hex_color = hex_match.group(1)
    
    # Convert hex to RGB
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    
    # Check if a > c > b (r > b > g)
    if r > b > g:
        new_hex = f"{r:02X}{b:02X}{g:02X}"
        return f"#{new_hex.lower()}"
    elif g > r > b:
        new_hex = f"{g:02X}{r:02X}{b:02X}"
        return f"#{new_hex.lower()}"
    elif g > b > r:
        new_hex = f"{g:02X}{b:02X}{r:02X}"
        return f"#{new_hex.lower()}"
    elif b > r > g:
        new_hex = f"{b:02X}{r:02X}{g:02X}"
        return f"#{new_hex.lower()}"
    elif b > g > r:
        new_hex = f"{b:02X}{g:02X}{r:02X}"
        return f"#{new_hex.lower()}"
    else:
        return hex_match.group(0)

def process_qss_file(input_path, output_path):
    # Read the QSS file
    with open(input_path, 'r') as file:
        qss_content = file.read()
    
    # Define regex patterns for RGB, RGBA, and HEX colors
    rgb_pattern = re.compile(r'rgb\((\d+,\s*\d+,\s*\d+)\)')
    rgba_pattern = re.compile(r'rgba\((\d+,\s*\d+,\s*\d+,\s*\d+)\)')
    hex_pattern = re.compile(r'#([0-9a-fA-F]{6})')
    
    # Replace colors according to the rules
    qss_content = rgb_pattern.sub(swap_rgb_values, qss_content)
    qss_content = rgba_pattern.sub(swap_rgba_values, qss_content)
    qss_content = hex_pattern.sub(swap_hex_values, qss_content)
    
    # Write the modified content back to a file
    with open(output_path, 'w') as file:
        file.write(qss_content)

# Example usage
input_file = 'base_stylesheet.txt'
output_file = 'base_stylesheet_new.txt'
process_qss_file(input_file, output_file)
