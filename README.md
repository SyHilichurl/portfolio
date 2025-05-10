# Portfolio Website

A modern, responsive portfolio website built with Flask, showcasing projects and skills.

## Features

- Responsive design that works on all devices
- Interactive project cards with detailed modals
- Skills section with categorized technologies
- Contact section with social links
- Smooth animations and transitions
- Project visualizations and metrics

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio.git
cd portfolio
```

2. Create a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
portfolio/
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── 1.jpg
│       ├── 2.jpg
│       └── 3.png
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Running the Application

1. Make sure your virtual environment is activated:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

2. Start the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Customization

### Adding Projects
To add a new project:
1. Add a new project card in `templates/index.html`
2. Add corresponding project details in the modal section
3. Add project images to `static/images/`

### Modifying Styles
- Main styles are in `static/css/style.css`
- Colors and variables are defined at the top of the CSS file

### Updating Content
- Edit `templates/index.html` to update text content
- Modify the skills section in the About section
- Update contact information in the Contact section

## Technologies Used

- Flask - Web framework
- HTML5 - Structure
- CSS3 - Styling
- JavaScript - Interactivity
- Font Awesome - Icons

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
