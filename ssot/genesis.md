# Genesis

Status: GENESIS

## Purpose
SSOT for trading monitoring + kill-switch system

## Current goal
- Ingest account data
- Monitor risk
- Trigger kill-switch

## Non-goals
- No ML
- No strategy engine
- No enterprise architecture

## Core object: AccountSnapshot
- account_id
- ts
- balance
- equity
- margin_used
- unrealized_pnl
- open_positions_count
