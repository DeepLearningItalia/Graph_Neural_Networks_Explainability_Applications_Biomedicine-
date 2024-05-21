# Graph Neural Networks and Explainability: Applications in Biomedicine
Reposity ufficiale del corso DLI di Graph Neural Networks and Explainability: Applications in Biomedicine.

## Per iniziare
La repository contiente un file ```environment.yml``` con tutti i pacchetti necessari per far funzionare i nootebook delle lezioni. Avendo [Anaconda](https://www.anaconda.com/) installato sul proprio computer, è possibile create un environment dal file. Aprite il file e modificate il parametro ```prefix``` con il percorso nel quale sono salvati i vostri enrivornment e lanciate da terminale:

```bash
conda env create -f environment.yml
```
Quando tutti i pacchetti saranno stati installati, attivate l'environment:

```bash
conda activate GNN_XAI_Biomedicine_env
```
Il nome di default dell'environment (GNN_XAI_Biomedicine_env) può essere modificato a piacimento.

## Contenuto
La repository contiene 6 notebook Python che seguondo le lezioni presentate nel corso. In particolare:

1. ```1-gene_disease_associations_via_GNNs.ipynb```: definizione, training e utilizzo di una graph neural network per la task di disease gene association discovery utilizzando una protein-protein interaction (PPI) network.
2. ```compound_activity_prediction_via_GNNs.ipynb```: definizione, training e utlizzo di una graph neural network per la task di compound activity predicion utilizzando dati molecolari.
3. ```3-protein_ligand_affinity_prediction_via_GNN.ipynb```: definizione, training e utilizzo di una graph neural network per la task di compound potency predicion utilizzando protein-ligand interaction graphs.
4. ```4-explaining_gene_disease_prioritization.ipynb```: utilizzo di XAI per spiegare le predizioni della graph neural network utlizzata per disease gene association discovery.
5. ```5-explaining_compound_activity_predictions.ipynb```: utilizzo di XAI per spiegare le predizioni della graph neural network utlizzata per compound activity predicion.
6. ```6-explaining_compound_potency_predictions.ipynb```: utilizzo di XAI per spiegare le predizioni della graph neural network utlizzata per compound potency predicion.
