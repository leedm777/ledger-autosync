import datetime
import time
from ofxclient.config import OfxConfig
import argparse
from ofxclient.client import Client
from formatter import Formatter
from ledgerautosync.sync import Synchronizer
from ledgerautosync.ledger import Ledger
import logging

def run(ledger, config):
    sync = Synchronizer(ledger)
    for acct in config.accounts():
        (ofx, txns) = sync.get_new_txns(acct,max_days=7)
        formatter = Formatter(acctid=ofx.account.account_id, currency=ofx.account.statement.currency, name=acct.description)
        for txn in txns:
            print formatter.format_txn(txn)

def run_default():
    logging.basicConfig(level=logging.DEBUG)
    ledger = Ledger()
    config = OfxConfig()
    run(ledger, config)

if __name__ == '__main__':
    run_default()