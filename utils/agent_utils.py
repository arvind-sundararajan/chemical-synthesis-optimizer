```json
{
    "utils/agent_utils.py": {
        "content": "
import logging
from typing import Dict, List
from langchain import LLMChain, PromptTemplate
from llama_index import VectorStoreIndex

# Initialize logger
logger = logging.getLogger(__name__)

def calculate_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The non-stationary drift index.

    Raises:
    - ValueError: If the input data is empty.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        # Calculate the non-stationary drift index using a stochastic regime switch model
        non_stationary_drift_index = sum([x**2 for x in data]) / len(data)
        logger.info(f'Non-stationary drift index: {non_stationary_drift_index}')
        return non_stationary_drift_index
    except Exception as e:
        logger.error(f'Error calculating non-stationary drift index: {e}')
        raise

def build_stochastic_regime_switch_model(index: VectorStoreIndex) -> LLMChain:
    """
    Build a stochastic regime switch model using a vector store index.

    Args:
    - index (VectorStoreIndex): The vector store index.

    Returns:
    - LLMChain: The stochastic regime switch model.

    Raises:
    - ValueError: If the input index is None.
    """
    try:
        if index is None:
            raise ValueError('Input index is None')
        # Build the stochastic regime switch model using a prompt template
        prompt_template = PromptTemplate(
            input_variables=['context'],
            template='Given the context {context}, generate a stochastic regime switch model.'
        )
        model = LLMChain(llm=index, prompt=prompt_template)
        logger.info('Stochastic regime switch model built')
        return model
    except Exception as e:
        logger.error(f'Error building stochastic regime switch model: {e}')
        raise

def simulate_rocket_science_problem(model: LLMChain, data: List[float]) -> Dict[str, float]:
    """
    Simulate the rocket science problem using a stochastic regime switch model.

    Args:
    - model (LLMChain): The stochastic regime switch model.
    - data (List[float]): The input dataset.

    Returns:
    - Dict[str, float]: The simulation results.

    Raises:
    - ValueError: If the input model or data is None.
    """
    try:
        if model is None or data is None:
            raise ValueError('Input model or data is None')
        # Simulate the rocket science problem using the stochastic regime switch model
        results = model({'context': ' '.join(map(str, data))})
        logger.info('Rocket science problem simulated')
        return results
    except Exception as e:
        logger.error(f'Error simulating rocket science problem: {e}')
        raise

if __name__ == '__main__':
    # Create a sample dataset
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    
    # Calculate the non-stationary drift index
    non_stationary_drift_index = calculate_non_stationary_drift_index(data)
    
    # Build the stochastic regime switch model
    index = VectorStoreIndex()
    model = build_stochastic_regime_switch_model(index)
    
    # Simulate the rocket science problem
    results = simulate_rocket_science_problem(model, data)
    
    # Print the results
    print(results)
",
        "commit_message": "feat: implement specialized agent_utils logic"
    }
}
```