# Automatic Pet Feeder Monitor

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

Automatic Pet Feeder Monitor is a Python-based project designed to monitor the food level in a cat feeder using an HC-SR04 distance sensor and a Raspberry Pi. The system checks the food level three times a day and sends an email alert when the food level is nearing empty/

## Features

- Measures food level using an HC-SR04 distance sensor.
- Sends email alerts when food levels are low.
- Checks food level three times daily.
- Handles sensor errors gracefully with retry logic.

## Requirements

- Raspberry Pi
- HC-SR04 Distance Sensor
- Python 3.x
- `smtplib` library for email alerts
- `RPi.GPIO` library for interacting with the GPIO pins
- `.env` file for email credentials

## Setup and Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/automatic-pet-feeder-monitor.git
   cd automatic-pet-feeder-monitor
   ```
2. **Create and configure `.env` file

   ```bash
   EMAIL_SENDER=your_email@gmail.com
   EMAIL_RECEIVER=receiver_email@gmail.com
   EMAIL_PASSWORD=your_email_password
   ```
3. **Install the required libraries**

   ```bash
   pip install RPi.GPIO
   ```
4. Run the script

   ```bash
   python script.py
   ```
