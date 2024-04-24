# Bitcoin Price Data Collection on AKS

This repository contains a Python script that fetches Bitcoin price data using the `yfinance` API and appends it to a CSV file. The script is designed to be run as a scheduled job in an Azure Kubernetes Service (AKS) cluster.

## Getting Started

These instructions will guide you through the process of setting up the Python script in a Docker container and deploying it to AKS.

### Prerequisites

- Azure CLI
- Docker
- `kubectl` configured to connect to your AKS cluster
- An Azure Container Registry (ACR)

### Installation

1. Clone this repository:

```sh
git clone https://github.com/varunkapuria96/btcprediction.git
cd btcprediction
```
2. Build the Docker image:
```sh

docker build -t <acrName>.azurecr.io/btc-price-collector:latest .
Push the Docker image to ACR:
```sh

az acr login --name <acrName>
docker push <acrName>.azurecr.io/btc-price-collector:latest
Replace <acrName> with the name of your Azure Container Registry.
```
Deploying to AKS
Ensure kubectl is configured with your AKS cluster context:
```sh

az aks get-credentials --resource-group <ResourceGroupName> --name <AKSClusterName>
```
Deploy the CronJob to AKS:
```sh

kubectl apply -f btc-price-fetcher-cronjob.yaml
```
Configuration
The btc-price-fetcher-cronjob.yaml file defines the CronJob resource for Kubernetes. Adjust the schedule as needed to determine when the job should run.

Usage
The script will automatically run at the scheduled time, fetch the Bitcoin prices from the past week, and append them to the BTC-USD.csv file in the current working directory.

License
This project is licensed under the MIT License.

Acknowledgments
Thanks to the yfinance library for providing an easy way to fetch financial data.
This workflow was inspired by the needs of cryptocurrency enthusiasts and data analysts.
