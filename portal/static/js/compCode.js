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
    "SyncOS Challenge": "SO",
    "Code Sprint": "CS",
    "Photography": "PH",
    "Reels competition": "RE",
    "Board games": "BG",
    "Scavenger hunt": "SH",
    "Fast Stock Exchange": "FS",
    "Line Following Robot (LFR) Competition": "LF",
    "Robo Soccer Competition": "RS",
    "Counter-Strike 2 (CS2)": "C2",
    "Sketching Competition": "SK",
    "Quiz competition": "QC",
    "Scrabble": "SC",
    "Chess": "CH",
    "Ludo": "LD",
}

function getCompetitionCode(competitionName) {
    if (competitionName in competitions) {
        return competitions[competitionName];
    } else {
        return null;
    }
}