import os
from dotenv import load_dotenv
from notion_client import Client
import calendar
load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

notion = Client(auth=NOTION_API_KEY)
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


# Function to create a new week page in the Notion database
def create_week(monday_date: str) -> None:
    notion.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties={
            "Name": {
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


fill_month(2025, 11)

