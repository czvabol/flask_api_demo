This tutorial describes how to create REST API in Python. The idea of this API originates from principles known in ASP .NET. Flask framework is used for API implementation. 

This demo builds an API for some basic mathematical operations like adding two numbers, adding days to a timestamp etc.

The example contains these features:
- controllers
- business logic provided in Dependency Injection container
- validation of input parameters
- logging
- application configuration
- the API is deployed into Docker image and running under ngnix

You can clone this demo from [GitHub](https://github.com/czvabol/flask_api_demo).

# Architecture
API is provided as a Python package called `demo_calculator`. It consists of the following subpackages:
- **abstract**, abstract classes which do the job of .NET interface (interfaces are not present in Python)
- **business**, business logic
- **controllers**, controllers - individual endpoints
- **exceptions**, exceptions
- **models**, data models used in business logic
- **dto**, data transfer objects

The architecture reminds MVC approach known from .NET. We have endpoints which are represented with controllers. The controllers accepts the requests from user and call business logic. Data transfer is performed through DTO. Dependency injection principle is used for this API. It means there are abstract classes for individual services. Their implementation can be easily replaced by different implementation. Python does not contain interfaces so abstract classes from ABC package are used instead.

# Abstract
Abstract classes are used instead of interfaces known from C#. Theses classes can be found in abstract package. There is an example of part of one class.
```
from abc import ABC, abstractmethod

class AbstractCalculator(ABC):
    @abstractmethod
    def add(self, a: float, b:float) -> float:
        """add two numbers

        Args:
            a (float): _description_
            b (float): _description_
        """
```

Abstract class is not a native part of Python. Package `abc` is required for using abstract classes.

# Business logic
This is an implementation of abstract classes. Implementation of business logic is here. There is a part of caclutaion service from the previous example.

```
from demo_calculator.abstract.abstract_calculator import AbstractCalculator


class Calculator(AbstractCalculator):

    def add(self, a: float, b: float) -> float:
        """Add two numbers

        Args:
            a (float): The first number
            b (float): The second number

        Returns:
            float: The sum of the two numbers
        """
        return a + b
```

#Controllers
There are multiple options how to create controllers for API. This demo uses `flask_restful` package. Each endpoint is represented by one class, e.g. `Addition` from package `addition` (file `demo_calculator/controllers/addition.py`). All the controllers used have a common predecessor `BackgroundResource`.  This class holds service container and logger. The services from the container can be then used inside each controller.

Controller class contains public methods for API services (get, post, ...). There is an example of controller for addition from previous examples.
```
from demo_calculator.dto.two_numbers_request import TwoNumbersRequest

class Addition(BackgroundResource):
    def post(self):
        requestData: TwoNumbersRequest = TwoNumbersRequest.parse_obj(request.json)

        service: AbstractCalculator = self.Container.Calculator
        logger = self.Container.Logger

        result = service.add(requestData.a, requestData.b)
        explanation = f'{requestData.a} + {requestData.b} = {result}'
        logger.debug(explanation)

        response = NumberResponse(result, explanation=explanation).to_dict()

`requestData` is taken from request body. The data is parsed into `TwoNumbersRequest` DTO. Then a service is taken from service container. Finally the business service response is transformed into DTO `NumberResponse` and returned. You can also see using of logger.


        return jsonify(response)
```

#Application
Flask api application is implemented in a file `app.py`. This file is like `program.cs` and `startup.cs` in C#. The API itself is represented by `Flask` instance. Controller infrastructure is build by wrapping this flask application into `Api` object.

You can see these steps inside this file:

- `Flask` instance is created. 
- Loading of configuration from `config.json` file. 
- Creation of logger.
- Creation of services.
- Adding services and logger into service container.
- Creation of API - `Api` instance.
- Adding of individual endpoints/controllers into API by calling method `add_resource`. Method parameters:
  - controller class
  - url of endpoint
  - arguments containing service container

Finally you can set port where the API is listening. In production the application is run in a different way.

# Input data validation
A framework `pydantic` is used for input data validation. DTOs inherit from `BaseModel` class. Doing this data type is verified when input data is being parsed. Data validation can also be added. There is an example of validation.
```
from pydantic import BaseModel, validator

class PositiveNumberRequest(BaseModel):
    number: float

    @validator('number')
    def number_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('number must be positive')
```

#Swagger
Flask API can also provide Swagger interface for documentation and testing. The information for Swagger must be structured in this case. It is not parsed automatically from code and summaries. `flasgger` package is used in this demo. Examples can be found directly in the code. 