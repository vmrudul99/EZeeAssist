# FranchiseSupplierNetwork Scrapy Project

## Introduction

FranchiseSupplierNetwork is a Scrapy project designed to scrape data from a franchise supplier network website. It includes a Spider named `FranchiseSupplierNetwork.py` located in the `spiders` folder, along with other essential files such as `pipelines.py`, `settings.py`, and `items.py`.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/vmrudul99/EZeeAssist.git
    ```

2. Navigate to the project directory:

    ```bash
    cd franchisesuppliernetwork
    ```

3. Install dependencies:

    ```bash
    pip install scrapy
    ```

## Usage

To run the Spider and scrape data, execute the following command in your command prompt or terminal:

```bash
scrapy crawl franchisesuppliernetwork -o data_resources_summary.csv

