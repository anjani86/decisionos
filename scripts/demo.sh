#!/bin/bash

BASE_URL="http://127.0.0.1:8000"

echo ""
echo "=============================================="
echo " DecisionOS — Supplier Decision Intelligence"
echo "=============================================="
echo ""

echo "1. API HEALTH"
echo "----------------------------------------------"
curl -s "$BASE_URL/health" | python -m json.tool

echo ""
echo "2. SUPPLIER A — ELIGIBLE DECISION"
echo "----------------------------------------------"

curl -s -X POST "$BASE_URL/decision" \
  -H "Content-Type: application/json" \
  -d '{
    "option_name": "STM32F407VGT6 - Supplier A",
    "criteria": [
      {"name": "Technical Fit", "weight": 0.25, "score": 90},
      {"name": "Availability", "weight": 0.20, "score": 90},
      {"name": "Lead Time", "weight": 0.15, "score": 95},
      {"name": "Price", "weight": 0.15, "score": 85},
      {"name": "Lifecycle", "weight": 0.10, "score": 95},
      {"name": "Supply Risk", "weight": 0.10, "score": 90},
      {"name": "Geographic Risk", "weight": 0.05, "score": 90}
    ],
    "lead_time_weeks": 8,
    "price": 10,
    "rohs_compliant": true,
    "lifecycle_status": "active",
    "hard_constraints": {
      "max_lead_time_weeks": 12,
      "max_price": 15,
      "rohs_required": true,
      "lifecycle_required": "active"
    }
  }' | python -m json.tool

echo ""
echo "3. SUPPLIER B — HARD CONSTRAINT FAILURE"
echo "----------------------------------------------"

curl -s -X POST "$BASE_URL/decision" \
  -H "Content-Type: application/json" \
  -d '{
    "option_name": "STM32F407VGT6 - Supplier B",
    "criteria": [
      {"name": "Technical Fit", "weight": 0.25, "score": 95},
      {"name": "Availability", "weight": 0.20, "score": 95},
      {"name": "Lead Time", "weight": 0.15, "score": 95},
      {"name": "Price", "weight": 0.15, "score": 95},
      {"name": "Lifecycle", "weight": 0.10, "score": 95},
      {"name": "Supply Risk", "weight": 0.10, "score": 95},
      {"name": "Geographic Risk", "weight": 0.05, "score": 95}
    ],
    "lead_time_weeks": 16,
    "price": 9,
    "rohs_compliant": true,
    "lifecycle_status": "active",
    "hard_constraints": {
      "max_lead_time_weeks": 12,
      "max_price": 15,
      "rohs_required": true,
      "lifecycle_required": "active"
    }
  }' | python -m json.tool

echo ""
echo "4. SUPPLIER COMPARISON"
echo "----------------------------------------------"

curl -s -X POST "$BASE_URL/comparison" \
  -H "Content-Type: application/json" \
  -d '{
    "options": [
      {
        "option_name": "STM32F407VGT6 - Supplier A",
        "criteria": [
          {"name": "Technical Fit", "weight": 0.25, "score": 90},
          {"name": "Availability", "weight": 0.20, "score": 90},
          {"name": "Lead Time", "weight": 0.15, "score": 95},
          {"name": "Price", "weight": 0.15, "score": 85},
          {"name": "Lifecycle", "weight": 0.10, "score": 95},
          {"name": "Supply Risk", "weight": 0.10, "score": 90},
          {"name": "Geographic Risk", "weight": 0.05, "score": 90}
        ],
        "lead_time_weeks": 8,
        "price": 10,
        "rohs_compliant": true,
        "lifecycle_status": "active",
        "hard_constraints": {
          "max_lead_time_weeks": 12,
          "max_price": 15,
          "rohs_required": true,
          "lifecycle_required": "active"
        }
      },
      {
        "option_name": "STM32F407VGT6 - Supplier B",
        "criteria": [
          {"name": "Technical Fit", "weight": 0.25, "score": 95},
          {"name": "Availability", "weight": 0.20, "score": 95},
          {"name": "Lead Time", "weight": 0.15, "score": 95},
          {"name": "Price", "weight": 0.15, "score": 95},
          {"name": "Lifecycle", "weight": 0.10, "score": 95},
          {"name": "Supply Risk", "weight": 0.10, "score": 95},
          {"name": "Geographic Risk", "weight": 0.05, "score": 95}
        ],
        "lead_time_weeks": 16,
        "price": 9,
        "rohs_compliant": true,
        "lifecycle_status": "active",
        "hard_constraints": {
          "max_lead_time_weeks": 12,
          "max_price": 15,
          "rohs_required": true,
          "lifecycle_required": "active"
        }
      }
    ]
  }' | python -m json.tool

echo ""
echo "=============================================="
echo " Demo complete"
echo "=============================================="