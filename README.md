# Automatic Pet Feeder Monitor

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

Automatic Pet Feeder Monitor is a Python-based project designed to monitor the food level in a cat feeder using an HC-SR04 distance sensor and a Raspberry Pi. The system checks the food level three times a day and sends email alerts when the food level is below a certain threshold.

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
