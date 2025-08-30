#!/usr/bin/env python3
"""
Test script to verify all imports work correctly
"""

try:
    print("Testing imports...")
    
    # Test basic imports
    import streamlit as st
    print("✓ Streamlit imported successfully")
    
    # Test LangChain imports
    from langchain_groq import ChatGroq
    print("✓ LangChain Groq imported successfully")
    
    from langgraph.graph import StateGraph, START, END
    print("✓ LangGraph imported successfully")
    
    from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
    print("✓ LangChain core messages imported successfully")
    
    # Test project imports
    from src.LGagenticai.ui.streamlitui.loadui import LoadStreamlitUI
    print("✓ LoadStreamlitUI imported successfully")
    
    from src.LGagenticai.LLMs.groqllm import groqllm
    print("✓ groqllm imported successfully")
    
    from src.LGagenticai.graph.gbuilder import builder
    print("✓ builder imported successfully")
    
    from src.LGagenticai.ui.streamlitui.display_result import Displayresultstreamlit
    print("✓ Displayresultstreamlit imported successfully")
    
    from src.LGagenticai.ui.streamlitui.uiconfigfile import Config
    print("✓ Config imported successfully")
    
    print("\n🎉 All imports successful! No import errors found.")
    
except ImportError as e:
    print(f"❌ Import Error: {e}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")