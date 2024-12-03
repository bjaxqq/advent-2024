# Advent of Code 2024

Although I have known about Advent of Code for a couple of years I never really gave it a try until now. This repository will be a place where I will put the code I wrote each day to get the correct answer.

## Automation script

Being a very lazy person (lol) I wanted to make an automation script that creates the necessary files I need each day (the python file I write code in and the input text). It creates a unique folder with the current day's date and then names the files appropriately.

### Running the script automatically

To get a quick start on the code when it comes out I created a line in my `crontab` to get the input and create the files right when the puzzle comes out. If you want to do this, here are the steps for MacOS/Linux and Windows:

#### MacOS/Linux

1. Open your terminal
2. Edit your crontab file

```bash
crontab -e
```

3. Add the following cron job

```bash
0 0 1-25 12 * /path/to/python /path/to/your/automation/script
```

This will make sure the code only runs during the Advent of Code time period and at 12:00 AM every day.

4. Save and exit

#### Windows

1. Open task scheduler

- You can do so by pressing `Windows + R` and entering `taskschd.msc`

2. Create a new task

- Press **Create task**
- General Tab:

  - Enter a name for the task, e.g., "Advent 2024 Auto Script".

- Triggers Tab:

  - Click **New**.
  - Set the **Begin the task** option to **On a schedule**.
  - Choose **Monthly** and set the **Start date** to December 1st.
  - Set the **End date to December 25th**.
  - Set the **Repeat task every** option to **1 day** for the duration of the period.
  - Set the **Start time** to 12:00 AM.
 
- Actions tab:

  - Click **New**, set **Action** to **Start a program**.
  - In the **Program/script box**, enter the path to Python (``C:\Python39\python.exe``, ``python3.exe``, etc.).
  - In the **Add** arguments (optional) box, enter the path to the Python script:
 
  ```text
  C:\Users\username\Developer\advent-2024\auto.py
  ```

- Finish

  - Click **OK** to save the task.
