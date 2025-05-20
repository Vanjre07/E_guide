# Entrepreneurship Guide Web Application

A comprehensive web application designed to help entrepreneurs learn, grow, and connect. Built with Python Flask, MongoDB, and modern web technologies.

## Features

### User Management
- User registration and authentication
- Role-based access control (Admin and User roles)
- Secure password handling
- User profile management

### Multi-language Support
- Bilingual interface (English and Kannada)
- Easy language switching
- Localized content

### Learning Resources
- Curated YouTube videos
- Educational articles
- Downloadable resources
- Resource categorization

### Q&A Forum
- User question submission
- Admin response system
- Question categorization
- Public forum for knowledge sharing

### Admin Dashboard
- User management
- Content moderation
- Resource management
- Analytics and insights

## Technical Stack

### Backend
- Python 3.9+
- Flask 2.0.1
- MongoDB
- Flask-Login
- Flask-WTF
- Flask-Babel

### Frontend
- HTML5
- CSS3 (Modern styling with animations)
- JavaScript (ES6+)
- Bootstrap 5
- Responsive design

### Database
- MongoDB
- PyMongo

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd entrepreneurship-guide
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up MongoDB:
- Install MongoDB on your system
- Start MongoDB service
- Create a database named 'entrepreneurship_guide'

5. Configure environment variables:
Create a `.env` file with:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
MONGODB_URI=mongodb://localhost:27017/entrepreneurship_guide
```

6. Run the application:
```bash
python app.py
```

## Project Structure

```
entrepreneurship-guide/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── static/
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # Main JavaScript file
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # User dashboard
│   ├── admin.html        # Admin dashboard
│   ├── forum.html        # Q&A forum
│   └── learning_resources.html  # Learning resources page
└── README.md             # Project documentation
```

## Features in Detail

### User Authentication
- Secure login system
- Password hashing
- Session management
- Remember me functionality

### Admin Features
- User management
- Content moderation
- Resource management
- Analytics dashboard
- Question answering system

### User Features
- Profile management
- Question submission
- Resource access
- Forum participation
- Language preference

### Learning Resources
- Video tutorials
- Articles and guides
- Downloadable materials
- Resource categorization
- Search functionality

### Q&A Forum
- Question submission
- Answer management
- Category organization
- Search functionality
- User interaction

## Styling and UI

The application features a modern, responsive design with:
- Clean and intuitive interface
- Smooth animations
- Responsive layout
- Modern color scheme
- Advanced hover effects
- Loading animations
- Form validation
- Interactive elements

## Security Features

- Password hashing
- CSRF protection
- Session management
- Input validation
- XSS prevention
- Secure headers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the development team.

## Acknowledgments

- Flask documentation
- MongoDB documentation
- Bootstrap documentation
- Contributors and maintainers

## Future Enhancements

- [ ] Real-time notifications
- [ ] Advanced analytics
- [ ] Mobile application
- [ ] Payment integration
- [ ] Social media integration
- [ ] Advanced search functionality
- [ ] User ratings and reviews
- [ ] Resource recommendations
- [ ] Community features
- [ ] API development
