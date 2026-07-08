from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Campaign:
    order_id: str
    campaign: str
    advertiser: Optional[str]
    publications: list[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    impressions: int = 0
    clicks: int = 0
    gam_url: str = ""