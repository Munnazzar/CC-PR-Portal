const competitions = {
    "all_competitions": "all_competitions",
    "Capture The Flag": "CF",
    "Competitive Programming": "CP",
    "Query Quest": "QQ",
    "Code in Dark": "CD",
    "PsuedoWar": "PW",
    "Speed Debugging": "SD",
    "UI/UX Design": "UX",
    "Data Visualization": "DV",
    "Web Dev": "WD",
    "Data Science": "DS",
    "AppDev": "AD",
    "SyncOS Challenge": "SO",
    "Code Sprint": "CS",
    "Photography": "PH",
    "Reels competition": "RE",
    "Board games": "BG",
    "Sketching Competition": "SK",
    "Podium game": "PG",
    "Scavenger hunt": "SH",
    "Fast Stock Exchange": "FS",
    "Robotics Competition": "RC",
    "Line Following Robot (LFR) Competition": "LF",
    "Robo Soccer Competition": "RS",
    "Counter-Strike 2 (CS2)": "C2",
    "Quiz competition": "QC"
}

function getCompetitionCode(competitionName) {
    if (competitionName in competitions) {
        return competitions[competitionName];
    } else {
        return null;
    }
}