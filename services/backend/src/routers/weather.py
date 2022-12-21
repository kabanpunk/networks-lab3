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
    prefix="/weather",
    tags=['Weather']
)


@router.get("/current", response_model=src.schemas.WeatherOut)
async def current(commons: src.schemas.WeatherQuery = Depends(src.schemas.WeatherQuery)):
    async with aiohttp.ClientSession() as session:
        query_dict = src.utils.dataclass_to_dict(commons)
        query_dict['appid'] = conf['OPENWEATHERMAP_API_KEY']
        async with session.get(
                '%s/weather' % conf['OPENWEATHERMAP_API_URL'],
                params=query_dict
        ) as resp:
            return src.schemas.WeatherOut.from_dict(await resp.json())


@router.get("/forecast", response_model=src.schemas.WeatherForecastOut)
async def forecast(commons: src.schemas.WeatherForecastQuery = Depends(src.schemas.WeatherForecastQuery)):
    async with aiohttp.ClientSession() as session:
        query_dict = src.utils.dataclass_to_dict(commons)
        query_dict['appid'] = conf['OPENWEATHERMAP_API_KEY']
        print(conf['OPENWEATHERMAP_API_URL'], query_dict)
        async with session.get(
                '%s/forecast' % conf['OPENWEATHERMAP_API_URL'],
                params=query_dict
        ) as resp:
            r = await resp.json()
            return src.schemas.WeatherForecastOut.from_dict(r)
