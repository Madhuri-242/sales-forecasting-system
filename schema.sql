CREATE DATABASE IF NOT EXISTS sales_forecast;
USE sales_forecast;

CREATE TABLE Territory (
    territory_id VARCHAR(20) PRIMARY KEY,
    territory_name VARCHAR(100) NOT NULL
);

CREATE TABLE SalesRep (
    rep_id VARCHAR(20) PRIMARY KEY,
    rep_name VARCHAR(100) NOT NULL,
    territory_id VARCHAR(20),
    FOREIGN KEY (territory_id)
        REFERENCES Territory(territory_id)
);

CREATE TABLE Account (
    account_id VARCHAR(20) PRIMARY KEY,
    account_name VARCHAR(100) NOT NULL,
    territory_id VARCHAR(20),
    FOREIGN KEY (territory_id)
        REFERENCES Territory(territory_id)
);

CREATE TABLE Stage (
    stage_name VARCHAR(50) PRIMARY KEY,
    probability DECIMAL(5,2) NOT NULL
);

INSERT INTO Stage (stage_name, probability) VALUES
('Prospecting', 0.10),
('Qualification', 0.25),
('Proposal', 0.50),
('Negotiation', 0.75),
('Closed Won', 1.00),
('Closed Lost', 0.00);

CREATE TABLE Opportunity (
    opp_id VARCHAR(30) PRIMARY KEY,
    account_id VARCHAR(20),
    rep_id VARCHAR(20),
    amount DECIMAL(12,2),
    stage VARCHAR(50),
    probability DECIMAL(5,2),
    forecast_amount DECIMAL(12,2),
    create_date DATE,
    expected_close_date DATE,
    actual_close_date DATE,
    close_date DATE,
    slippage_days INT,
    opportunity_age INT,
    is_stale CHAR(1),
    FOREIGN KEY (account_id) REFERENCES Account(account_id),
    FOREIGN KEY (rep_id) REFERENCES SalesRep(rep_id),
    FOREIGN KEY (stage) REFERENCES Stage(stage_name)
);

CREATE TABLE ForecastSnapshot (
    snapshot_id VARCHAR(30) PRIMARY KEY,
    opp_id VARCHAR(30),
    snapshot_date DATE,
    forecast_amount DECIMAL(12,2),
    probability DECIMAL(5,2),
    FOREIGN KEY (opp_id) REFERENCES Opportunity(opp_id)
);

CREATE TABLE StageHistory (
    stage_history_id VARCHAR(40) PRIMARY KEY,
    opp_id VARCHAR(30),
    stage_name VARCHAR(50),
    change_date DATE,
    FOREIGN KEY (opp_id) REFERENCES Opportunity(opp_id),
    FOREIGN KEY (stage_name) REFERENCES Stage(stage_name)
);

CREATE TABLE Activity (
    activity_id VARCHAR(30) PRIMARY KEY,
    opp_id VARCHAR(30),
    rep_id VARCHAR(20),
    activity_type VARCHAR(20),
    activity_date DATE,
    FOREIGN KEY (opp_id) REFERENCES Opportunity(opp_id),
    FOREIGN KEY (rep_id) REFERENCES SalesRep(rep_id)
);

CREATE TABLE HistoricalBooking (
    booking_id VARCHAR(30) PRIMARY KEY,
    opp_id VARCHAR(30),
    booking_amount DECIMAL(12,2),
    booking_date DATE,
    FOREIGN KEY (opp_id) REFERENCES Opportunity(opp_id)
);

CREATE TABLE Quota (
    quota_id VARCHAR(50) PRIMARY KEY,
    rep_id VARCHAR(20),
    quarter VARCHAR(10),
    target_amount DECIMAL(12,2),
    FOREIGN KEY (rep_id) REFERENCES SalesRep(rep_id)
);

CREATE TABLE TerritoryHistory (
    history_id VARCHAR(30) PRIMARY KEY,
    rep_id VARCHAR(20),
    old_territory_id VARCHAR(20),
    new_territory_id VARCHAR(20),
    change_date DATE,
    FOREIGN KEY (rep_id) REFERENCES SalesRep(rep_id),
    FOREIGN KEY (old_territory_id) REFERENCES Territory(territory_id),
    FOREIGN KEY (new_territory_id) REFERENCES Territory(territory_id)
);