from typing import List

from fastapi import APIRouter, Request, Depends
from dataclasses import dataclass, asdict

import src.schemas
import src.utils

from src.config import conf

import json

import aiohttp
import asyncio
import os

router = APIRouter(
    prefix="/places",
    tags=['Places']
)


@router.get("/", response_model=src.schemas.GeoCodeOut)
async def geocode(commons: src.schemas.GeoCodeQuery = Depends(src.schemas.GeoCodeQuery)):
    async with aiohttp.ClientSession() as session:
        query_dict = src.utils.dataclass_to_dict(commons)
        query_dict['key'] = conf['GRAPHHOPPER_API_KEY']
        async with session.get(
                conf['GRAPHHOPPER_API_URL'],
                params=query_dict
        ) as resp:
            return src.schemas.GeoCodeOut.from_dict(await resp.json())
