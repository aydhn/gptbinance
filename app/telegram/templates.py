from typing import Dict, Any

class TelegramTemplates:
    @staticmethod
    def get_template(template_name: str) -> str:
        return f"Template: {template_name}"
