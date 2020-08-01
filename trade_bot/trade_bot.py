""" main function of repo """


from db import populate_db, update_db
from analyze import analyze


def trade_bot():
    # main control flow

    # only populates/creates db if it doesn't already exist
    populate_db()

    # main loop
    while True:
        update_db()
        analyze()


if __name__ == '__main__':
    trade_bot()
