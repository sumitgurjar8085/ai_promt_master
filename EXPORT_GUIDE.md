# AI Prompt Master - Export & Build Guide

This guide details how to export the project, build the Android APK/AAB, configure Google AdMob, and run the Python Flet application.

---

## 1. Downloading / Exporting the Project as a ZIP

In **Google AI Studio**:
1. Locate the top navigation bar or the project settings menu (the three dots `⋮` or the project settings icon in the header).
2. Click **Download Project as ZIP** (or **Export to GitHub** if you prefer version control).
3. Extract the downloaded `.zip` file on your local machine.

---

## 2. Building the Android APK

### Prerequisites
- **JDK 17+** (Java Development Kit)
- **Android Studio** (Ladybug / Koala / Hedgehog or newer) or Android SDK Command-line Tools

### Step-by-Step Command Line Build:
Open a terminal in the root project folder:

```bash
# Make gradlew executable (macOS / Linux)
chmod +x gradlew

# Build the Debug APK
./gradlew assembleDebug

# On Windows:
# gradlew.bat assembleDebug
```

The compiled APK will be generated at:
```
app/build/outputs/apk/debug/app-debug.apk
```
You can transfer this `.apk` directly to any Android phone or drag-and-drop it onto an emulator to install it.

### Building a Signed Release APK / AAB:
1. Open the project in **Android Studio**.
2. Go to **Build** > **Generate Signed Bundle / APK...**
3. Select **Android App Bundle** (for Google Play Store) or **APK** (for direct distribution).
4. Select your keystore (or create a new release keystore).
5. Choose destination folder and build type `release`.

---

## 3. Configuring Production Google AdMob

The codebase is pre-configured with Google's official Test Ad Unit IDs so ads work right out of the box during testing without account suspensions.

When you are ready to publish:
1. Visit [Google AdMob Console](https://admob.google.com) and create your app and ad units (Rewarded Video and Banner).
2. In `app/src/main/AndroidManifest.xml`:
   Replace the test Application ID with your real AdMob App ID:
   ```xml
   <meta-data
       android:name="com.google.android.gms.ads.APPLICATION_ID"
       android:value="ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX" />
   ```
3. In `app/src/main/java/com/example/admob/AdMobConfig.kt`:
   Paste your live Ad Unit IDs into:
   ```kotlin
   productionAppId = "ca-app-pub-XXXXXXXXXXXXXXXX~XXXXXXXXXX"
   productionRewardedAdUnitId = "ca-app-pub-XXXXXXXXXXXXXXXX/XXXXXXXXXX"
   productionBannerAdUnitId = "ca-app-pub-XXXXXXXXXXXXXXXX/XXXXXXXXXX"
   ```

---

## 4. Running the Python Flet Cross-Platform App

The repository includes the complete standalone Python Flet implementation in `app_data.py` and `main.py`.

### Installation & Execution:
```bash
# 1. Install Python 3.9+ and Flet
pip install flet

# 2. Run the application
python main.py
```

### Packaging Python Flet as Android/iOS/Desktop:
```bash
# Package as desktop app
flet pack main.py --name "AIPromptMaster"

# Build for Android via Flet CLI:
flet build apk
```
