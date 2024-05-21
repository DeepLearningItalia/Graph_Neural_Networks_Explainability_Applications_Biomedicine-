### Module implementing utils functions ###
### Author: Andrea Mastropietro © All rights reserved ###

import torch
from torch_geometric.data import InMemoryDataset
from torch_geometric.utils import from_networkx   

import numpy as np
from sklearn.model_selection import train_test_split

import networkx as nx


def create_edge_index(mol, weighted=False):
    """
    Create edge index for a molecule.
    """
    adj = nx.to_scipy_sparse_array(mol).tocoo()
    row = torch.from_numpy(adj.row.astype(np.int64)).to(torch.long)
    col = torch.from_numpy(adj.col.astype(np.int64)).to(torch.long)
    edge_index = torch.stack([row, col], dim=0)

    if weighted:
        weights = torch.from_numpy(adj.data.astype(np.float32))
        edge_weight = torch.FloatTensor(weights)
        return edge_index, edge_weight

    return edge_index

class ChemicalDataset(InMemoryDataset):
    '''
    Class for the PyG version of the dataset.
    '''
    def __init__(self, root, transform=None, pre_transform=None, pre_filter=None, data_list = None):
        super().__init__(root, transform, pre_transform, pre_filter)
        
        self.data_list = data_list

        self.data, self.slices = self.collate(data_list)

class GDADataset(InMemoryDataset):
	def __init__(self, G, labels, attributes, num_classes=2):
		super(GDADataset, self).__init__('.', None, None, None)

		# import data from the networkx graph with the attributes of the nodes
		data = from_networkx(G, attributes)
			
		y = torch.from_numpy(np.array(labels)).type(torch.long)

		data.x = data.x.float()
		data.y = y.clone().detach()
		data.num_classes = num_classes

		# Using train_test_split function from sklearn to stratify train/test/val sets
		indices = range(G.number_of_nodes())
		# Stratified split of train/test/val sets. Returned indices are used to create the masks
		X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(data.x, data.y, indices, test_size=0.3, stratify=labels, random_state=42)
		# To create validation set, test set is splitted in half
		X_test, X_val, y_test, y_val, test_idx, val_idx = train_test_split(X_test, y_test, test_idx, test_size=0.5, stratify=y_test, random_state=42)

		n_nodes = G.number_of_nodes()
		train_mask  = torch.zeros(n_nodes, dtype=torch.bool)
		test_mask   = torch.zeros(n_nodes, dtype=torch.bool)
		val_mask    = torch.zeros(n_nodes, dtype=torch.bool)
		
		for idx in train_idx:
			train_mask[idx] = True

		for idx in test_idx:
			test_mask[idx] = True
		
		for idx in val_idx:
			val_mask[idx] = True

		data['train_mask']  = train_mask
		data['test_mask']   = test_mask
		data['val_mask']    = val_mask

		self.data, self.slices = self.collate([data])