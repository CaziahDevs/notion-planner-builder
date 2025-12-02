import os
from dotenv import load_dotenv
from notion_client import Client
import calendar
load_dotenv()

# Helper function to format Notion IDs
def format_notion_id(raw_id: str) -> str:
    return f"{raw_id[:8]}-{raw_id[8:12]}-{raw_id[12:16]}-{raw_id[16:20]}-{raw_id[20:]}"

NOTION = Client(auth=os.environ["NOTION_KEY"])
NOTION_PAGE_ID = format_notion_id(os.environ["NOTION_PAGE_ID"])
cal = calendar.Calendar()

week_template = [
    {
        "object": "block",
        "type": "column_list",
        "column_list": {
            "children": [
                # Column 1: Days of the week
                {
                    "object": "block",
                    "type": "column",
                    "column": {
                        "children": [
                            # Monday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Mon"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            },
                            # Tuesday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Tue"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            },
                            # Wednesday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Wed"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            },
                            # Thursday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Thu"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            },
                            # Friday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Fri"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            },
                            # Saturday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Sat"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            },
                            # Sunday
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Sun"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "to_do",
                                "to_do": {
                                    "rich_text": [],
                                    "checked": False
                                }
                            }
                        ]
                    }
                },
                # Column 2: Notes
                {
                    "object": "block",
                    "type": "column",
                    "column": {
                        "children": [
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Notes"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": []
                                }
                            }
                        ]
                    }
                },
                # Column 3: Quick Links
                {
                    "object": "block",
                    "type": "column",
                    "column": {
                        "children": [
                            {
                                "object": "block",
                                "type": "heading_3",
                                "heading_3": {
                                    "rich_text": [{"type": "text", "text": {"content": "Quick Links"}}]
                                }
                            },
                            {
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": [
                                        {
                                            "type": "text",
                                            "text": {"content": "Write, press 'space' for AI, '/' for commands..."}
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
]



# Fill the month with week pages
def fill_month(year: int, month: int) -> None:
    # function to grab the mondays in a month
    def get_mondays_in_month(year: int, month: int) -> list[str]:
        month_list = cal.monthdatescalendar(year, month)

        mondays: list[str] = []
        for week in month_list:
            mondays.append(week[0].strftime("%B %d"))

        return mondays

    mondays:list[str] = get_mondays_in_month(year, month)
    for week_number, monday in enumerate(mondays, start=1):
        try:
            create_week(monday, week_number)
        except Exception as e:
            print(f"Error creating week for {monday}: {e}")
    return



# Function to create a new week page in the Notion database
def create_week(monday_date: str, week_number: int) -> None:
    # Map week numbers to emoji
    week_emojis = {
        1: "1️⃣",
        2: "2️⃣", 
        3: "3️⃣",
        4: "4️⃣",
        5: "5️⃣"
    }

    NOTION.pages.create(
        parent={
            "page_id": NOTION_PAGE_ID
            },
        icon={
            "type": "emoji",
            "emoji": week_emojis.get(week_number, "🗓️")
        },
        properties={
            "title": {
                "title": [
                    {
                        "type": "text",
                        "text": {"content": f"Week of {monday_date}"}
                    }
                ]
            }
        },
        children=week_template
    )


fill_month(2025, 12)

