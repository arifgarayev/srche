# Yandex Go Android App Driver Data Scraper

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue.svg)](https://linkedin.com/in/garayevarif/)

> **Disclaimer**: This project is for educational purposes only. Please respect GDPR regulations, in particular, [Article 8 of the Charter of Fundamental Rights of the European Union](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:12012P/TXT&from=EN).

---

## Overview

Yandex Go Android Driver Data Scraper is a powerful Python-based project designed for scraping driver data from the Yandex Go Android ridesharing application.

This scraper orders fake cash trips registering fake rider account in the Yandex Go Android mobile app. It has the feature to bypass both client-level and device-level (UUID) blocks.


---

## Key Features

- **Efficient Data Scraping**: This bot is capable of scraping all necessary driver information displayed on the UI view of the Yandex Go Android app. It extracts data, from the drivers' mobile number to Yandex partner information, ensuring a comprehensive driver details.

- **OTP Handling**: To register an account on the Yandex Go platform, the bot issues an online virtual number and receive OTPs verification using the [sms-activate.org](sms-activate.org) service's API.

- **Database**: All scraped data is securely stored in a PostgreSQL database, providing easy access and management of the collected information.

- **Configuration**: Customize the bot's behavior by editing configuration files located in the `/src/config` folder.

  - Replace `ServiceAccountToken` with a valid Google Service Account for an integration with Google Sheets or other Google Cloud services.
  - Database connection string in `database_config.json`, and emulator configurations in `emulator_config.json`. You can also modify the `top_routes.json` file to define country - city - origin-destination routes of your fake trips.

- **Deployment**: Execute the scraper either on an Android virtual device or on a real mobile device with USB debugging enabled. It seamlessly connects to real Android device.

- **Server**: The script starts a node server automatically and ensures that populated ports are freed in case of any process crashes.

- **Workflow**: The script follows a procedural approach, including app reinstallation steps after every 7 fake orders within a user account.

---

## Installation

1. Clone this repository to your local machine.
2. Install JDK, Android Studio (Android API) - [More about environment setting](https://anivaz.medium.com/how-to-set-up-appium-with-android-studio-for-mobile-app-testing-a300b7910364)
3. Install the specific APK version of the Yandex Go Android application to your Android OS device from the `/apk` folder.

---

## Entity Diagram

Here's an overview of the key entities in the database:

```plaintext
class common_table {
   bigint mobile_no
   bigint portal_id
   bigint uber_confirmation
   bigint yango_confirmation
   timestamp end_date
   bigint uber_trips_completed
   bigint yango_trips_completed
   integer id
}

class uber_driver_data {
   text name
   text number
   timestamp date
   integer id
   text details
}

class uber_number {
   integer id
   bigint mobile_no
   bigint portal_id
   bigint confirmation
   integer trips_completed
}

class yango_driver_data {
   text name
   text number
   timestamp date
   integer id
   text details
}

class yango_number {
   integer id
   bigint mobile_no
   bigint portal_id
   bigint confirmation
   integer trips_completed
}
```

---

## Usage

1. Configure the scraper by editing the relevant files in the `/src/config` folder.
2. Execute the scraper on an Android virtual device or a real Android device with USB debugging enabled.

---

## License

This repository is licensed under the MIT License - see the [MIT License](https://mit-license.org/) file for details.

