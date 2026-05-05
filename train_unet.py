import torch
from models.unet import UNet

model = UNet()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.BCELoss()

# Dummy training loop (replace with dataset)
for epoch in range(5):
    x = torch.randn(1,1,512,512)
    y = torch.randn(1,1,512,512)

    pred = model(x)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.item()}")
