_layer = None

def set_layer(layer_to_remember):
    global _layer
    _layer = layer_to_remember

def get_layer():
    return _layer