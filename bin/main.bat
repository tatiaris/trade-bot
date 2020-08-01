@ECHO OFF
SET start_dir=%cd%
CD trade_bot
python -c "from trade_bot import trade_bot; trade_bot()"
CD %start_dir%
