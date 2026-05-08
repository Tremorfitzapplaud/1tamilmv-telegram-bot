#!/usr/bin/env python3
"""
1TamilMV Telegram Bot - Main Entry Point
The #1 Telegram Bot for Tamil Movies, OTT Updates & Movie Information
"""

import os
import sys
import logging
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from bot import TamilMVBot
from config import Config, setup_logging


def main():
    """Main entry point for the bot"""
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("="*60)
    logger.info("🎬 1TamilMV Telegram Bot v3.0.0")
    logger.info("The #1 Telegram Bot for Tamil Movies")
    logger.info("="*60)
    
    try:
        # Load configuration
        logger.info("📋 Loading configuration...")
        config = Config()
        config.load()
        
        # Verify bot token
        if not config.bot_token:
            logger.error("❌ Bot token not found in config.yaml")
            logger.error("Please set BOT_TOKEN in config.yaml or environment variable")
            sys.exit(1)
        
        logger.info(f"✅ Configuration loaded successfully")
        logger.info(f"Bot Username: @{config.bot_username}")
        
        # Initialize bot
        logger.info("🤖 Initializing bot...")
        bot = TamilMVBot(config)
        
        # Setup database
        logger.info("💾 Setting up database...")
        bot.setup_database()
        
        # Register handlers
        logger.info("📡 Registering command handlers...")
        bot.register_handlers()
        
        # Start bot
        logger.info("🚀 Starting bot...")
        print("\n")
        print("╔" + "═"*58 + "╗")
        print("║" + " "*58 + "║")
        print("║" + "  🎬 1TamilMV Telegram Bot v3.0.0".center(58) + "║")
        print("║" + "  Your Gateway to Tamil Cinema".center(58) + "║")
        print("║" + " "*58 + "║")
        print("║" + f"  Bot: @{config.bot_username}".ljust(58) + "║")
        print("║" + "  Status: RUNNING ✅".ljust(58) + "║")
        print("║" + " "*58 + "║")
        print("╚" + "═"*58 + "╝")
        print("\n")
        
        # Start polling
        bot.start()
        
    except KeyboardInterrupt:
        logger.info("\n👋 Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
