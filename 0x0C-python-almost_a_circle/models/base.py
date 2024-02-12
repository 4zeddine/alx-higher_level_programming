#!/usr/bin/python3
"""Defines the class Base"""
import json
import csv
import turtle


class Base:
    """Base class model.

    private class attribute:
        __nb_objects (int): number of Base instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing new Base

        Args:
            id (int): identification of a Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON serialization of a list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON serialization of a list_objs to a file.

        Args:
            list_objs (list): list of instances who inherits of Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the deserialization of a JSON string.

        Args:
            json_string (str): string representing a list of dictionaries.
        Returns:
            if json_string is None or empty an empty list.
            Otherwise the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(10, 10)
            else:
                new = cls(10)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances.

        reads from a file `<Class name>.json`.

        Returns:
            if the file does not exist an empty list.
            Otherwise a list of instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list from a CSV file.

        Reads from `<Class name>.csv`.

        Returns:
            if the file does not exist an empty list.
            Otherwise a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws Rectangles and Squares.

        Args:
            list_rectangles (list): a list of Rectangle objects to draw.
            list_squares (list): a list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#17181a")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ced9ed")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#f7cbb7")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
