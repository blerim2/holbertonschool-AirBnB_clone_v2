#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            list_of_cities = []

            for key, value in storage.all(City).items():
                if value.to_dict()['state_id'] == self.id:
                    list_of_cities.append(value)
            return list_of_cities
