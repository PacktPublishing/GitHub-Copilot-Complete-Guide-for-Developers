# Chatbot Application

This project is a simple chatbot application that utilizes the OpenAI API to provide conversational capabilities. The application is structured to separate concerns, making it easy to maintain and extend.

## Project Structure

```
chatbot-app
├── src
│   ├── app.ts                # Entry point of the application
│   ├── services
│   │   └── openaiService.ts  # Service for interacting with OpenAI API
│   ├── controllers
│   │   └── chatController.ts  # Controller for handling chat requests
│   └── types
│       └── index.ts          # Type definitions for requests and responses
├── package.json               # NPM package configuration
├── tsconfig.json              # TypeScript configuration
└── README.md                  # Project documentation
```

## Installation

To install the necessary dependencies, run:

```
npm install
```

## Usage

To start the application, use the following command:

```
npm start
```

## API Endpoints

The application exposes the following API endpoint:

- `POST /chat`: Sends a message to the chatbot and receives a response.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.