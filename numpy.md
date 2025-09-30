# Numpy functions

### 1) Array Creation
```
np.array()
np.zeros(shape)
np.ones(shape)
np.empty(shape)
np.full(shape, value)
np.arange(start, stop, step)
np.linspace(start, stop, num)
np.logspace(start, stop, num)
np.eye(n)
np.identity(n)
np.random.rand(shape)
np.random.randn(shape)
np.random.randint(low, high, size)
np.random.choice(arr, size)
```
### 2) Array Inspection
```
arr.shape
arr.ndim
arr.size
arr.dtype
arr.itemsize
arr.nbytes
np.info(obj)
```

### 3) Array Manipulation
```
np.reshape(arr, newshape)
np.resize(arr, newshape)
np.ravel(arr)
arr.flatten()
np.transpose(arr)
arr.T
np.moveaxis(arr, source, dest)
np.swapaxes(arr, axis1, axis2)
np.expand_dims(arr, axis)
np.squeeze(arr)
np.concatenate([a, b], axis)
np.stack([a, b], axis)
np.hstack([a, b])
np.vstack([a, b])
np.split(arr, indices_or_sections)
np.array_split(arr, sections)
np.hsplit(arr, sections)
np.vsplit(arr, sections)
```

### 4) Mathematical Operations
```
np.add(a, b)
np.subtract(a, b)
np.multiply(a, b)
np.divide(a, b)
np.floor_divide(a, b)
np.power(a, b)
np.mod(a, b)
np.remainder(a, b)
np.abs(a)
np.negative(a)
np.sign(a)
np.sqrt(a)
np.cbrt(a)
np.square(a)
np.exp(a)
np.log(a)
np.log10(a)
np.log2(a)
np.sin(a)
np.cos(a)
np.tan(a)
np.arcsin(a)
np.arccos(a)
np.arctan(a)
np.deg2rad(a)
np.rad2deg(a)
np.round(a)
np.floor(a)
np.ceil(a)
np.clip(arr, min, max)
```

### 5) Statistics
```
np.min(arr)
np.max(arr)
np.argmin(arr)
np.argmax(arr)
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.percentile(arr, q)
np.quantile(arr, q)
np.corrcoef(arr)
np.cov(arr)
```

### 6) Linear Algebra
```
np.dot(a, b)
np.matmul(a, b)
np.vdot(a, b)
np.inner(a, b)
np.outer(a, b)
np.cross(a, b)
np.linalg.inv(a)
np.linalg.det(a)
np.linalg.matrix_rank(a)
np.linalg.eig(a)
np.linalg.eigvals(a)
np.linalg.norm(a)
np.linalg.solve(a, b)
np.trace(a)
```

### 7) Indexing & Selection
```
arr[i]
arr[i:j]
arr[:, i]
arr[i, :]
arr[::step]
np.where(condition)
np.nonzero(arr)
np.take(arr, indices)
np.put(arr, indices, values)
np.extract(condition, arr)
```

### 8) Random Functions
```
np.random.seed(n)
np.random.rand(d0, d1, ...)
np.random.randn(d0, d1, ...)
np.random.randint(low, high, size)
np.random.random(size)
np.random.choice(arr, size)
np.random.permutation(arr)
np.random.shuffle(arr)
np.random.uniform(low, high, size)
np.random.normal(mean, std, size)
np.random.binomial(n, p, size)
np.random.poisson(lam, size)
```
